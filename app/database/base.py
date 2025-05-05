from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# This replaces the Base from your original database.py
# All your models will inherit from this Base