# Deployment Guide for Student Management Application

## Overview

This document provides a step-by-step guide to deploying the Student Management Application to a cloud platform. We will outline the process for deploying to Heroku, as it provides a straightforward setup for small applications and is ideal for this project. 

## Prerequisites

Before proceeding, ensure that you have completed the following:

- Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) on your local machine.
- Have a [Heroku account](https://signup.heroku.com/) set up.
- Install **Docker** to containerize your application.

## Deployment Steps

### Step 1: Initialize Your Project

1. Navigate to the root directory of your application.

### Step 2: Create a `Dockerfile`

Create a `Dockerfile` at the root of your project to define how your application will be built inside a container. Below is a basic example:

```dockerfile
# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file at first to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-dev

# Copy the rest of the application code
COPY . /app/

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Step 3: Create a `docker-compose.yml`

Provide orchestration for your application and PostgreSQL database by creating a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgres://user:password@db:5432/studentsdb
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: studentsdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Step 4: Deploying to Heroku

1. **Login to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a new Heroku application**:
   ```bash
   heroku create <your-app-name>
   ```

3. **Set up Heroku PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Configure environment variables**:
   Set the database URL in Heroku:
   ```bash
   heroku config:set DATABASE_URL=$(heroku config:get DATABASE_URL)
   ```

5. **Deploy your application**:
   - First, build the Docker image and push it to Heroku:
   ```bash
   heroku container:push web --app <your-app-name>
   ```
   - Then release the container:
   ```bash
   heroku container:release web --app <your-app-name>
   ```

### Step 5: Access Your Application

- Once deployed, you can access your application via:
```bash
https://<your-app-name>.herokuapp.com
```

### Step 6: Verify Your Setup

- Ensure that your application is running properly by accessing the endpoints:
  - POST `/students`
  - GET `/students`
  - GET `/students/{id}`

### Monitoring and Logging

Heroku provides built-in logging capabilities, which you can access with the following command:
```bash
heroku logs --tail --app <your-app-name>
```

## Conclusion

By following the steps outlined in this guide, you will have successfully deployed the Student Management Application on Heroku with PostgreSQL as the database. Ensure to monitor the performance and stability using Heroku’s management dashboard or integrated logging features.