from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.session import engine
from .database import models

# Initialize the FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers after app creation to avoid circular imports
from .api.v1.auth import router as auth_router
from .api.v1.workouts import router as workout_router

# Include routers with proper prefixes
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    workout_router,
    prefix="/api/workouts",
    tags=["Workouts"]
)