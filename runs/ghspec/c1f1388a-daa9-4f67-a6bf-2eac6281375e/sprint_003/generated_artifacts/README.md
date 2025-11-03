# README.md

# Project Title

Description of the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Database Migration](#database-migration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables as per `.env.example`.

## Usage

To start the application, run:

```
uvicorn src.main:app --reload
```

## API Documentation

### Course Endpoints

This project introduces a new Course entity and corresponding API endpoints.

#### Create a Course

- **Endpoint:** `POST /courses`
- **Request Body:**
  ```json
  {
    "name": "Course Name", 
    "level": "Beginner"
  }
  ```
- **Response:** 
  - Status: `201 Created`
  - Body:
  ```json
  {
    "id": 1,
    "name": "Course Name",
    "level": "Beginner"
  }
  ```

#### Get a Course by ID

- **Endpoint:** `GET /courses/{id}`
- **Response:** 
  - Status: `200 OK`
  - Body:
  ```json
  {
    "name": "Course Name",
    "level": "Beginner"
  }
  ```
  
#### Get All Courses

- **Endpoint:** `GET /courses`
- **Response:**
  - Status: `200 OK`
  - Body:
  ```json
  [
    {
      "id": 1,
      "name": "Course Name",
      "level": "Beginner"
    },
    {
      "id": 2,
      "name": "Another Course",
      "level": "Intermediate"
    }
  ]
  ```

## Database Migration

The database has been updated to include a new `courses` table with the following attributes:
- `name`: required string field
- `level`: required string field

Migrations have been implemented to add the Course table while ensuring that existing data in the Student table remains intact. Refer to the database management section for details on migration commands.

## Contributing

To contribute to this project, please fork the repository and create a new branch for your feature. Ensure that your code adheres to the existing style and includes necessary tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.