from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

# Add explicit API prefix
app = FastAPI()

from fastapi import APIRouter

router = APIRouter()



app.include_router(
    router,
    prefix="/api",  # Add this line
    tags=["workouts"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add these endpoints directly under the app
# Remove /api prefix from endpoint definitions
@app.post("/workouts/", response_model=list[schemas.WorkoutSet])
def create_workout_sets(sets: list[schemas.WorkoutSetCreate], db: Session = Depends(get_db)):
    return crud.create_multiple_sets(db=db, sets=sets)

@app.get("/workouts/", response_model=list[schemas.WorkoutSet])
def read_workouts(db: Session = Depends(get_db)):
    return crud.get_workout_sets(db)

# Updated PUT endpoint
@app.put("/workouts/{set_id}", response_model=schemas.WorkoutSet)
def update_set(
    set_id: int,
    workout_set: schemas.WorkoutSetCreate,
    db: Session = Depends(get_db)
):
    db_set = db.query(models.WorkoutSet).filter(models.WorkoutSet.id == set_id).first()
    if not db_set:
        raise HTTPException(status_code=404, detail="Set not found")
    
    for field, value in workout_set.dict().items():
        setattr(db_set, field, value)
    
    db.commit()
    db.refresh(db_set)
    return db_set

# Updated DELETE endpoint
@app.delete("/workouts/{set_id}")
def delete_set(set_id: int, db: Session = Depends(get_db)):
    db_set = db.query(models.WorkoutSet).filter(models.WorkoutSet.id == set_id).first()
    if not db_set:
        raise HTTPException(status_code=404, detail="Set not found")
    
    db.delete(db_set)
    db.commit()
    return {"detail": "Set deleted"}

# Add CORS middleware if needed
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)