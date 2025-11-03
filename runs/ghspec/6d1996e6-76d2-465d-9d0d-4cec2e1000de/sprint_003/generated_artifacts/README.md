# README.md

# Course Management API

## Overview
The Course Management API allows for the management of courses within the educational institution. It enables the creation, retrieval, and updating of course entities to facilitate better organization and tracking of the courses offered.

## API Endpoints

### 1. Create Course
- **Endpoint**: `POST /courses`
- **Request Body**: 
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  - `name` (string, required): The name of the course.
  - `level` (string, required): The academic level of the course.
  
- **Response**: 
  - **201 Created**: Returns the created course object in JSON format.
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

### 2. Retrieve Course
- **Endpoint**: `GET /courses/{id}`
- **Response**: 
  - **200 OK**: Returns the course object in JSON format:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  - **404 Not Found**: If the ID does not exist.

### 3. Update Course
- **Endpoint**: `PUT /courses/{id}`
- **Request Body**: 
  ```json
  {
    "name": "Advanced Programming",
    "level": "Intermediate"
  }
  ```
  - `name` (string, optional): The new name of the course.
  - `level` (string, optional): The new academic level of the course.
  
- **Response**:
  - **200 OK**: Returns the updated course object in JSON format:
  ```json
  {
    "id": 1,
    "name": "Advanced Programming",
    "level": "Intermediate"
  }
  ```
  - **404 Not Found**: If the ID does not exist.

## Database Schema
A new "courses" table should be created in the database with the following columns:
- `name`: String, required field to store course names.
- `level`: String, required field to store the academic level of the course. 

## Purpose
The purpose of this feature is to create a new Course entity within the system to facilitate the organization and management of courses offered by the educational institution. This addition will enhance the capability to manage educational programs, allowing for better categorization and tracking of courses. By incorporating a Course entity with a name and level fields, the application will support academic planning and student enrollment activities more effectively.