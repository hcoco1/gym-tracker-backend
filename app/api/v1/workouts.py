# app/api/v1/workouts.py
from datetime import datetime, timezone  # Add timezone to imports
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Absolute imports (recommended)
from app.database.session import get_db
from app.database.models import WorkoutSet, User
from app.schemas.workouts import WorkoutSetCreate, WorkoutSetResponse, Message
from app.api.v1.auth import get_current_user

router = APIRouter()

def create_workout_set(db: Session, workout_set: WorkoutSetCreate, user_id: int) -> WorkoutSet:
    """Helper function to create workout set"""
    db_set = WorkoutSet(
        **workout_set.model_dump(),  # Changed from .dict() for Pydantic v2
        user_id=user_id,
        date=datetime.now(timezone.utc)  # Correct usage of timezone
    )
    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return db_set

@router.post("/", response_model=list[WorkoutSetResponse], status_code=status.HTTP_201_CREATED)
async def create_workout_sets(
    sets: list[WorkoutSetCreate],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> list[WorkoutSetResponse]:
    """Create multiple workout sets"""
    return [
        create_workout_set(db, workout_set, current_user.id)
        for workout_set in sets
    ]

@router.get("/", response_model=list[WorkoutSetResponse])
async def read_workouts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> list[WorkoutSetResponse]:
    """Get all workout sets for current user"""
    return db.query(WorkoutSet).filter(
        WorkoutSet.user_id == current_user.id
    ).all()

@router.put("/{set_id}", response_model=WorkoutSetResponse)
async def update_workout_set(
    set_id: int,
    workout_set: WorkoutSetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> WorkoutSetResponse:
    """Update a specific workout set"""
    db_set = db.query(WorkoutSet).filter(
        WorkoutSet.id == set_id,
        WorkoutSet.user_id == current_user.id
    ).first()
    
    if not db_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout set not found"
        )
    
    for field, value in workout_set.model_dump().items():
        setattr(db_set, field, value)
    
    db.commit()
    db.refresh(db_set)
    return db_set

@router.delete("/{set_id}", response_model=Message)
async def delete_workout_set(
    set_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Message:
    """Delete a workout set"""
    db_set = db.query(WorkoutSet).filter(
        WorkoutSet.id == set_id,
        WorkoutSet.user_id == current_user.id
    ).first()
    
    if not db_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout set not found"
        )
    
    db.delete(db_set)
    db.commit()
    return {"message": "Workout set deleted successfully"}