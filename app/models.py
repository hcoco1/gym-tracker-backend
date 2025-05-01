from sqlalchemy import Column, Integer, String, Date
from datetime import date
from .database import Base

class Workout(Base):
    __tablename__ = "workouts"
    
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    workout_date = Column(Date, default=date.today())  # Match the schema change