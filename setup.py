from setuptools import setup, find_packages

setup(
    name="gymtracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'sqlalchemy',
        'pydantic',
        'alembic',
        'python-dotenv'
    ],
)