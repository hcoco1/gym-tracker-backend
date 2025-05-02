from sqlalchemy.orm import Session
from . import models, schemas

def create_workout_set(db: Session, workout_set: schemas.WorkoutSetCreate):
    db_set = models.WorkoutSet(**workout_set.dict())
    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return db_set

def get_workout_sets(db: Session):
    return db.query(models.WorkoutSet).all()

# crud.py
def create_multiple_sets(db: Session, sets: list[schemas.WorkoutSetCreate]):
    db_sets = [models.WorkoutSet(**set.dict()) for set in sets]
    db.add_all(db_sets)
    db.commit()
    
    # Refresh each object to get database-generated values
    for db_set in db_sets:
        db.refresh(db_set)
    
    return db_sets