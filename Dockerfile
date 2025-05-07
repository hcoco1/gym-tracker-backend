# Use the official Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy dependency file first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (excluding what's in .dockerignore)
COPY . .

# Expose FastAPI port (default is 8000)
EXPOSE 8000

# Command to run your app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

