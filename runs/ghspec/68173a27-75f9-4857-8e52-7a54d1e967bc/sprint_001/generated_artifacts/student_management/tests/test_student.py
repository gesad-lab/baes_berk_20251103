# Dockerfile to package the Student Management application

# Use the official Python image to create a lightweight container with FastAPI
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt ./

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY src/ ./src/
COPY tests/ ./tests/

# Expose the port that the FastAPI app runs on
# Default FastAPI runs on 8000
EXPOSE 8000

# Command to run the FastAPI application
# Using uvicorn server, specify app location and host
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]