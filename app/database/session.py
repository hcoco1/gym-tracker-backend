from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load environment variables from .env
load_dotenv()

# Validate environment variables
required_env_vars = ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DB_NAME']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
    logger.error(error_msg)
    raise RuntimeError(error_msg)

# Construct the SQLAlchemy connection string with SSL
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    "?sslmode=require"
    "&sslrootcert=prod-ca-2021.crt"  # Supabase's CA certificate
)

# Configure database engine with connection pooling
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=300,  # Recycle connections every 5 minutes
    connect_args={
        'keepalives': 1,
        'keepalives_idle': 30,
        'keepalives_interval': 10,
        'keepalives_count': 5
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

def verify_database_connection():
    """Test database connection with exponential backoff"""
    import time
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            logger.info("✅ Database connection successful")
            return
        except SQLAlchemyError as e:
            logger.warning(f"⚠️ Connection attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_attempts - 1:
                logger.critical("❌ Failed to connect to database after %d attempts", max_attempts)
                raise
            time.sleep(2 ** attempt)

# Verify connection on startup
verify_database_connection()

def get_db():
    """Dependency for getting DB session with automatic cleanup"""
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        logger.error(f"Database error occurred: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()