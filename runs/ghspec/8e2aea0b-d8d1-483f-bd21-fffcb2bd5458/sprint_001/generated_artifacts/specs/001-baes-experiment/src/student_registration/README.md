# student_registration/README.md

# Student Registration API

This project is a simple API for managing student registrations. It allows users to create, read, update, and delete student records.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Environment Variables](#environment-variables)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/student_registration.git
   ```

2. Navigate into the project directory:
   ```bash
   cd student_registration
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a `.env` file in the root directory and populate it with your configuration settings (as detailed in the **Environment Variables** section below).

2. Run the application:
   ```bash
   python src/app.py
   ```

## API Endpoints

- **POST /students**: Register a new student.
- **GET /students**: Retrieve a list of registered students.
- **GET /students/{id}**: Retrieve a student by ID.
- **PUT /students/{id}**: Update a student's information.
- **DELETE /students/{id}**: Remove a student from the registry.

## Testing

To run the tests, execute:
```bash
pytest tests/
```

## Environment Variables

The following environment variables should be defined in your `.env` file:

- `DATABASE_URL`: The connection string for your database. This is required for connecting to the database for storing student records.
  - Example: `DATABASE_URL=postgresql://username:password@localhost:5432/student_db`

Make sure to replace `username`, `password`, and `student_db` with your actual database credentials.
  
- Additional environment variables for configuration may be added as the project grows. Make sure to document them here as needed.

```text
# Example of .env file
DATABASE_URL=postgresql://username:password@localhost:5432/student_db
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.
