from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/workouts/", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db, workout)

@app.get("/workouts/", response_model=list[schemas.Workout])
def read_workouts(db: Session = Depends(get_db)):
    return crud.get_workouts(db)

# PUT endpoint
@app.put("/workouts/{workout_id}", response_model=schemas.Workout)
def update_workout(
    workout_id: int,
    workout: schemas.WorkoutCreate,
    db: Session = Depends(get_db)
):
    db_workout = db.query(models.Workout).filter(models.Workout.id == workout_id).first()
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    for field, value in workout.dict().items():
        setattr(db_workout, field, value)
    
    db.commit()
    db.refresh(db_workout)
    return db_workout

# DELETE endpoint
@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = db.query(models.Workout).filter(models.Workout.id == workout_id).first()
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    db.delete(db_workout)
    db.commit()
    return {"detail": "Workout deleted"}