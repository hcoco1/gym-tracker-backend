from pydantic import BaseModel
from datetime import datetime

class WorkoutSetBase(BaseModel):
    exercise: str
    set_number: int
    reps: int
    weight: float
    day: str
    type: str

class WorkoutSetCreate(WorkoutSetBase):
    pass

class WorkoutSetResponse(WorkoutSetBase):
    id: int
    date: datetime
    user_id: int

    class Config:
        from_attributes = True

class Message(BaseModel):
    message: str