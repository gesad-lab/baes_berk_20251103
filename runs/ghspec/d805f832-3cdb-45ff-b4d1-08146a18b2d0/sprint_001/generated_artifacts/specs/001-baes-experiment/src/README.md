# README.md

# Student Management API

This is a simple API for managing students. It allows you to create and retrieve student records. The application is built using FastAPI and uses SQLite as the database.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/student-management-api.git
   cd student-management-api
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables if necessary (refer to `.env.example`).

### Running the Application

You can start the application by running:
```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Create a Student

- **Endpoint**: `POST /students`
- **Description**: Create a new Student.
- **Input**: JSON object with a required field `name` (string).
- **Successful Response**: HTTP status 201 with a JSON object containing the ID and `name` of the created Student.
  
**Example Request**:
```json
{
    "name": "John Doe"
}
```

**Example Response**:
```json
{
    "id": 1,
    "name": "John Doe"
}
```

### 2. Retrieve a Student

- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieve a Student by ID.
- **Successful Response**: HTTP status 200 with a JSON object containing the ID and `name` of the Student.

**Example Response**:
```json
{
    "id": 1,
    "name": "John Doe"
}
```

### Error Handling

- **Creating a Student without a Name**:
    - **Request**: If a user sends a request to create a Student without a `name`, the application will return an error response.
    - **Error Response**: HTTP status 400 indicating that the name is required.
  
### Automatic Database Schema Creation

On application startup, the SQLite database schema will be created automatically if it does not already exist. It will include a `students` table with the necessary fields.

## Usage Scenarios

1. **Creating a Student**: A user sends a request to create a Student with a valid name, and the API returns a success response with the created student data.

2. **Retrieving a Student**: A user retrieves the details of an existing Student by ID, and the API returns the student's name and ID in JSON format.

3. **Creating a Student without a Name**: If a user attempts to create a Student without providing a name, the API will return an error response indicating that the name is required.

4. **Validating Automatic Schema Creation**: The application starts without pre-existing schemas in the database, resulting in the database schema being automatically created on startup.

## Contributing

Feel free to submit issues or pull requests for improvements. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.