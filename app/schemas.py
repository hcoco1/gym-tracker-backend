from pydantic import BaseModel
from datetime import date

class WorkoutBase(BaseModel):
    exercise: str
    sets: int
    reps: int
    workout_date: date = date.today()  # Changed from 'date' to 'workout_date'

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    
    class Config:
        orm_mode = True