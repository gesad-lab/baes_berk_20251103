# Updated Content of README.md

---
# Project Overview

This project aims to manage course and teacher associations while preventing schedule conflicts. This document outlines the API endpoints, database schema, and key functionalities.

## Functional Requirements

1. **Course-Teacher Association**:
   - Update the Course entity to include a relationship field to the Teacher entity:
     - `teacher_id: Integer` (Foreign key referencing Teacher id)

2. **Database Schema Update**:
   - Implement a migration script to support the new relationship with the Teacher table.

3. **RESTful API Endpoints**:
   - A **PATCH** endpoint `/courses/{course_id}`:
     - Update an existing course with a teacher association.
     - Accepts JSON payload:
       ```json
       {
           "teacher_id": "integer"
       }
       ```
   - A **GET** endpoint `/courses/{course_id}`:
     - Returns course details, including associated teacher information.

4. **Validation Logic**:
   - Implement validation to prevent assigning a teacher to multiple overlapping courses, ensuring effective teaching assignments.

5. **Database Migration**:
   - Ensure that existing Course and Teacher data remains intact during this integration.

## User Scenarios & Testing

1. **Scenario: Associate a teacher with a course**
   - As an admin user, I want to associate an existing teacher with a course.
   - **Test**: Verify that selecting a teacher from a list and saving changes updates the course record correctly.

2. **Scenario: Check course details**
   - As an admin user, I want to check course details and view the associated teacher's information.
   - **Test**: Ensure the course detail view accurately displays the associated teacher's information.

3. **Scenario: Validate course assignment**
   - As an admin user, I want to prevent assigning a teacher to multiple overlapping courses.
   - **Test**: Confirm that an error message appears if attempting to assign a teacher to overlapping courses.

## Technical Plan

1. **Database Migration**:
   - Implement a migration script to add the `teacher_id` column to the Course table:
     ```python
     async def migrate_course_teachers():
         async with aiosqlite.connect("database.db") as db:
             await db.execute("ALTER TABLE course ADD COLUMN teacher_id INTEGER REFERENCES teacher(id);")
             await db.commit()
     ```

2. **API Endpoints Creation**:
   - Define RESTful endpoints in `api/courses.py` to handle the association between courses and teachers.
     ```python
     from fastapi import APIRouter, HTTPException
     from .models.courses import CourseUpdateRequest, CourseResponse
     import aiosqlite
     
     router = APIRouter()
     
     @router.patch("/courses/{course_id}", response_model=CourseResponse)
     async def update_course(course_id: int, request: CourseUpdateRequest):
         async with aiosqlite.connect("database.db") as db:
             # Validate conditions for overlapping course assignments
             overlapping_courses = await validate_teacher_schedule(request.teacher_id, course_id)
             if overlapping_courses:
                 raise HTTPException(status_code=400, detail="Teacher assigned to overlapping courses.")
             
             # Proceed to update the course
             result = await db.execute(
                 "UPDATE course SET teacher_id = ? WHERE id = ?",
                 (request.teacher_id, course_id)
             )
             if result.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Course not found or update conflict occurred.")
             await db.commit()
     
             # Return the updated course details
             return await get_course_by_id(course_id)
     
     async def get_course_by_id(course_id: int):
         async with aiosqlite.connect("database.db") as db:
             cursor = await db.execute("SELECT id, name, level, teacher_id FROM course WHERE id = ?", (course_id,))
             course = await cursor.fetchone()
             return CourseResponse(id=course[0], name=course[1], level=course[2], teacher_id=course[3])
     
     async def validate_teacher_schedule(teacher_id: int, course_id: int):
         # Logic to find overlapping courses scheduled for the same teacher
         async with aiosqlite.connect("database.db") as db:
             query = """
             SELECT * FROM course 
             WHERE teacher_id = ? AND id != ? AND (start_time < end_time AND end_time > start_time)
             """
             cursor = await db.execute(query, (teacher_id, course_id))
             return await cursor.fetchall()
     ```

3. **Testing Plan**:
   - Write tests to cover the new API functionality.
   - Ensure tests validate the overlap condition and functionality of the PATCH and GET endpoints.

## Success Criteria

1. The existing database schema reflects the new relationship between Course and Teacher without data loss.
2. The application provides clear error messages when assigning teachers to overlapping schedules.

---

