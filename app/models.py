from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import date
from .database import Base
from datetime import datetime


class Workout(Base):
    __tablename__ = "workouts"
    
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float, nullable=True)  # New field
    duration = Column(Integer, nullable=True)  # New field (minutes)
    notes = Column(String, nullable=True)  # New field
    date = Column(DateTime, default=datetime.utcnow)  # Existing field