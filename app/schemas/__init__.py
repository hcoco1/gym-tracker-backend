# app/schemas/__init__.py
from .auth import UserBase, UserCreate, UserResponse, Token, TokenData
from .workouts import WorkoutSetBase, WorkoutSetCreate, WorkoutSetResponse, Message

__all__ = [
    'UserBase',
    'UserCreate',
    'UserResponse',
    'Token',
    'TokenData',
    'WorkoutSetBase',
    'WorkoutSetCreate',
    'WorkoutSetResponse',
    'Message'
]