from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base
from models import Course, Teacher

# Create a new FastAPI instance
app = FastAPI()

# Custom function to include additional OpenAPI documentation
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Course & Teacher API",
        version="1.0.0",
        description="API to manage Courses and Teachers. Allows assignment and retrieval of Teachers related to Courses.",
        routes=app.routes,
    )
    
    # Update description for the Course assignment endpoints
    openapi_schema["paths"]["/courses/{course_id}/assign-teacher"] = {
        "post": {
            "summary": "Assign a Teacher to a Course",
            "description": "Assign a teacher to a specific course by its ID.",
            "parameters": [
                {
                    "name": "course_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "integer"},
                },
                {
                    "name": "teacher_id",
                    "in": "body",
                    "required": True,
                    "schema": {"type": "integer"},
                }
            ],
            "responses": {
                200: {"description": "Teacher assigned successfully"},
                404: {"description": "Course or Teacher not found"},
                409: {"description": "Course already has a teacher assigned"},
            },
        }
    }
    
    openapi_schema["paths"]["/courses/{course_id}"] = {
        "get": {
            "summary": "Retrieve a Course by ID",
            "description": "Get details of a course including assigned teacher if any.",
            "parameters": [
                {
                    "name": "course_id",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "integer"},
                }
            ],
            "responses": {
                200: {
                    "description": "Course details retrieved successfully",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "integer"},
                                    "title": {"type": "string"},
                                    "teacher": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "integer"},
                                            "name": {"type": "string"},
                                            "email": {"type": "string"},
                                        },
                                    },
                                },
                            }
                        }
                    },
                },
                404: {"description": "Course not found"},
            },
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Include the API routes (assuming other related routes are included)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Initialize TestClient for testing
client = TestClient(app)