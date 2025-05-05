from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base

class WorkoutSet(Base):
    __tablename__ = "workout_sets"
    
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String(100), nullable=False)
    set_number = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    day = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationship to User
    user = relationship("User", back_populates="workouts")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to WorkoutSet
    workouts = relationship("WorkoutSet", back_populates="user", cascade="all, delete-orphan")
