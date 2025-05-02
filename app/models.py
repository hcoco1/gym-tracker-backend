from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from .database import Base

class WorkoutSet(Base):
    __tablename__ = "workout_sets"
    
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String)
    set_number = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)
    day = Column(String)
    type = Column(String)
    date = Column(DateTime, nullable=False)
