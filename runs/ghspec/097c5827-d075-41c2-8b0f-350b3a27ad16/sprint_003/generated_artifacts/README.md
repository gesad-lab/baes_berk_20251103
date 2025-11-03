# README.md

# Course Application

This is a Course Application built using Flask. It allows users to manage courses, students, and other related entities through a RESTful API.

## Project Structure

```plaintext
course_app/
│
├── src/
│   ├── app.py                   # Main application entry point
│   ├── models.py                # SQLAlchemy models (includes Course)
│   ├── controllers/
│   │   ├── course_controller.py  # New file for managing Course requests
│   ├── services/
│   │   ├── course_service.py     # New file for Course business logic
│   └── database.py               # Database initialization & migrations
│
├── tests/
│   ├── test_course.py            # Unit tests for Course functionality
│
├── requirements.txt              # Dependency file
└── README.md                     # Project documentation
```

## Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Testing**: pytest
- **API Documentation**: OpenAPI/Swagger (for optional documentation generation)

## API Endpoints

### Courses

#### Create a Course

`POST /courses`

This endpoint allows the creation of a new course.

**Request Body**:
```json
{
    "title": "Introduction to Programming",
    "description": "Learn the basics of programming."
}
```

**Response**:
- **201 Created**: Returns the created course object.
- **400 Bad Request**: If the request body is invalid or missing required fields.

---

#### Get Courses

`GET /courses`

Retrieves a list of all courses.

**Response**:
- **200 OK**: Returns an array of course objects.
- **500 Internal Server Error**: If there is an issue retrieving courses.

---

#### Get a Course

`GET /courses/{id}`

Retrieves a single course by its ID.

**Path Parameters**:
- `id` (integer): The ID of the course.

**Response**:
- **200 OK**: Returns the course object.
- **404 Not Found**: If the course does not exist.

---

#### Update a Course

`PUT /courses/{id}`

Updates an existing course.

**Path Parameters**:
- `id` (integer): The ID of the course.

**Request Body**:
```json
{
    "title": "Updated Course Title",
    "description": "Updated description."
}
```

**Response**:
- **200 OK**: Returns the updated course object.
- **400 Bad Request**: If the request body is invalid.
- **404 Not Found**: If the course does not exist.

---

#### Delete a Course

`DELETE /courses/{id}`

Deletes a course by its ID.

**Path Parameters**:
- `id` (integer): The ID of the course.

**Response**:
- **204 No Content**: If the course is deleted successfully.
- **404 Not Found**: If the course does not exist.

---

## Setup

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up the database using the commands in `database.py`.
4. Start the application with `python src/app.py`.

## Testing

Run tests using pytest:

```bash
pytest
```

This documentation provides an overview of using the Course Application API, detailing endpoints, request and response formats, and basic setup instructions.