backend/
├── .env                    # Environment variables
├── app/                    # Main application package
│   ├── __init__.py         # Package initialization
│   ├── main.py             # FastAPI app creation and config
│   ├── config.py           # Configuration settings
│   ├── database/           # Database-related files
│   │   ├── __init__.py
│   │   ├── base.py         # Base model
│   │   ├── session.py      # Session handling
│   │   └── models.py       # SQLAlchemy models
│   ├── api/                # API endpoints
│   │   ├── __init__.py
│   │   ├── v1/             # Version 1 of API
│   │   │   ├── __init__.py
│   │   │   ├── auth.py     # Authentication routes
│   │   │   └── workouts.py # Workout routes
│   ├── core/               # Core application logic
│   │   ├── __init__.py
│   │   ├── security.py     # Auth utilities
│   │   └── exceptions.py   # Custom exceptions
│   ├── schemas/            # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── auth.py         # Auth schemas
│   │   └── workouts.py     # Workout schemas
│   ├── utils/              # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py      # Helper functions
│   └── dependencies.py     # FastAPI dependencies
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_workouts.py
├── alembic/                # Database migrations (if using)
│   ├── versions/
│   └── env.py
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation