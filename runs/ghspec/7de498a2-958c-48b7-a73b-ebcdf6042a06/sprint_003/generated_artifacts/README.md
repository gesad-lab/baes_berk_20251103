# README.md

# Project Title

## Overview

This project is a FastAPI application that allows users to create and manage courses easily. It supports various operations such as creating, retrieving, and updating course details.

## Setup and Configuration

### Environment Variables

Make sure to set up the environment variables required for the application to function properly, including database connection strings and API keys.

### Running Migrations on Startup

To ensure that the database migrations are executed automatically on application startup, we have integrated migration commands into the Docker startup process. Ensure to have the following steps in place:

1. Within your `Dockerfile`, ensure the entry point commands include migration scripts. This will use Alembic or any configured migration tool to apply migrations automatically when the container starts.
  
   An example Dockerfile configuration is as follows:

   ```dockerfile
   # Dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY . /app
   RUN pip install -r requirements.txt
   CMD ["bash", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]
   ```

2. Make sure your `docker-compose.yml` also reflects the need to run migrations before starting the FastAPI application.

   Example section in `docker-compose.yml` could look like:

   ```yaml
   version: '3.8'
   services:
     app:
       build: .
       ports:
         - "8000:8000"
       environment:
         - DATABASE_URL=postgresql://user:password@db:5432/mydatabase
       depends_on:
         - db
   ```

3. The migration tool should be configured to point to the correct database and handle schema updates for the newly added Course entity without affecting existing data.

### Starting the Application

Once the above configurations are made, you can start your application along with the migrations using Docker:

```bash
docker-compose up --build
```

This command builds the application image and runs the migrations on startup, ensuring your database schema is always up-to-date with your models.

## Usage

After starting the application, you can interact with the course management API endpoints documented in `src/api.py`. 

## Tests

The project includes a suite of tests to ensure the integrity of functionality. To run the tests, use `pytest`:

```bash
pytest
```
Make sure that your test database is configured correctly in your environment.

## Contribution

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

---
