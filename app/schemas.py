from pydantic import BaseModel
from datetime import datetime

class WorkoutSetBase(BaseModel):
    exercise: str
    set_number: int
    reps: int
    weight: float
    day: str
    type: str
    date: datetime  # Add this line

class WorkoutSetCreate(BaseModel):
    exercise: str
    set_number: int
    reps: int
    weight: float
    day: str
    type: str
    date: datetime  # Make this field required

class WorkoutSet(WorkoutSetBase):
    id: int
    
    class Config:
        from_attributes = True