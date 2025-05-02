from pydantic import BaseModel
from datetime import date
from typing import Optional
from datetime import datetime

class WorkoutBase(BaseModel):
    exercise: str
    sets: int
    reps: int
    weight: Optional[float] = None
    duration: Optional[int] = None
    notes: Optional[str] = None
    date: Optional[datetime] = None

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    
    class Config:
        from_attributes = True