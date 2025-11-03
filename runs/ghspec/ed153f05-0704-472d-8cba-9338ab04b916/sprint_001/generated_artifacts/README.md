# Student Management System

This project is a backend API for managing student records. It includes functionality for adding, retrieving, and managing student data. The API is built using Flask and utilizes SQLite for database storage. 

## Setup Instructions

### Prerequisites

- Python 3.x
- pipenv (for managing packages)

### Create the Virtual Environment

1. Navigate to the project directory.
2. Run the following command to create a virtual environment and install dependencies:

   ```bash
   pipenv install
   ```

3. Create a `.env` file for configuration settings. You can refer to `.env.example` for the required settings.

### Running the Application

1. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

2. Run the application:

   ```bash
   python src/app.py
   ```

The API will start running locally, and you can use tools like Postman or curl to interact with it.

## API Endpoints

- **POST /students** - Create a new student record.
- **GET /students/{id}** - Retrieve a student record by ID.
- **GET /students** - Retrieve all student records.

## Testing

To run tests, execute the following command in the terminal:

```bash
pytest
```

Make sure to cover both success and error cases, aiming for at least 70% test coverage.

## Future Improvements

### Monitoring & Logging

- Implement structured logging that logs API request and response details for better traceability and debugging.
- Integrate a monitoring solution to keep track of application performance and errors.
- Use an external service for logging errors and monitoring system health.
- Document the logging and monitoring approach in future updates to this README.

## License

This project is licensed under the MIT License - see the LICENSE file for details.