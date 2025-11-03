# README.md

# Student Management Web Application

## Overview

This application manages student data, allowing CRUD operations on student information, as well as monitoring the application status through a health check endpoint.

## API Endpoints

### Health Check Endpoint

- **GET** `/health`
  
  This endpoint checks the health status of the application. It returns a simple JSON response indicating the application is healthy.

#### Response Format

```json
{
  "status": "healthy",
  "uptime": "total_uptime_in_seconds"
}
```

#### Example Response

```json
{
  "status": "healthy",
  "uptime": "12345"
}
```

### Setup and Configuration

#### Environment Variables

To run this application, create a `.env` file in the root directory of the project with the following settings:

```
# Example .env settings
DATABASE_URL=<your_database_url>
SECRET_KEY=<your_secret_key>
```

Make sure to keep your `.env` file out of version control by adding it to your `.gitignore`.

## Running the Application

To start the application, run:

```bash
# Start the server
python app.py
```

## Testing

To ensure everything works as intended, write and run tests for the endpoints and business logic. Use a testing framework like `pytest`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.