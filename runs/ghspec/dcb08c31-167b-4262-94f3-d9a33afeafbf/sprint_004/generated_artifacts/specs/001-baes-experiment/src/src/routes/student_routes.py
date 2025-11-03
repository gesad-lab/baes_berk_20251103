# README.md

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing application. This enhancement will enable students to be associated with one or more courses, thereby allowing for better tracking of student enrollment and progress in their educational journey. This aligns with user needs for an efficient management system that organizes courses against student profiles, setting the foundation for future functionalities such as enrollment tracking, course completion rates, and reporting.

## Functional Requirements

1. **Establish Relationship**
   - Define a many-to-many relationship between the Student and Course entities, allowing a student to enroll in multiple courses and each course to be attended by multiple students.

2. **Database Schema Update**
   - The database schema has been updated to include a join table named `student_courses`, which captures the relationship with the following fields:
     - `student_id`: Integer (Foreign Key referencing Student)
     - `course_id`: Integer (Foreign Key referencing Course)

3. **Database Migration**
   - A database migration has been executed to create the new `student_courses` table while preserving all existing data in the Student and Course tables.

4. **API Endpoints**
   - **POST /students/{studentId}/courses**
     - This endpoint allows you to associate multiple courses with a specified student by accepting a JSON body containing an array of course IDs. On success, it returns the updated student object including the associated courses.

   - **GET /students/{studentId}/courses**
     - This endpoint retrieves the list of all courses associated with the specified student, including details for each course.

5. **JSON Responses**
   - All API responses maintain JSON format, including the associated course details in success and error messages.