# README.md

# Student Entity Web Application

## Overview

The Student Entity Web Application is designed to manage student records efficiently. It allows users to create, retrieve, update, and delete student information. 

## New Email Feature

### Purpose

As part of the enhancements to the application, a new email field has been added to the Student entity. This feature aims to improve student data management by allowing users to store and retrieve email addresses alongside student names. The implementation of this feature ensures more comprehensive student records, meeting the evolving needs of user data management.

### User Scenarios

1. **Scenario: Create a Student with Email**
   - Given a user has access to the application,
   - When the user submits a name and an email for a new student,
   - Then the student should be successfully created and stored in the database with both name and email.
   - **Test Case**: Verify that a student with the provided name and email is retrievable after creation.

2. **Scenario: Retrieve Student Information including Email**
   - Given a user knows an existing student ID,
   - When the user requests the student information,
   - Then the application should return the student's details in JSON format, including their email.
   - **Test Case**: Verify that the returned JSON includes the correct email along with the student's name.

3. **Scenario: Update a Student's Email**
   - Given a user has access to an existing student's ID,
   - When the user submits a new email to update the student’s information,
   - Then the application should update the student’s record in the database.
   - **Test Case**: Verify that the student's email is updated correctly.

4. **Scenario: Attempt to Create a Student without Email**
   - Given a user has access to the application,
   - When the user attempts to create a new student with a name but without an email,
   - Then the application should return an error message indicating that the email is a required field.
   - **Test Case**: Verify that appropriate error messages are returned for missing the email field.

### API Endpoints Update

The following API endpoints have been updated to incorporate the new email field functionality:

- **POST** `/students`
  - Request body must include both `name` and `email`:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

- **GET** `/students/{id}`
  - The response will now include the email field:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

- **PUT** `/students/{id}`
  - The request body can now include a new email for modification:
  ```json
  {
    "email": "john.doe@example.com"
  }
  ```

### Conclusion

This new email feature not only enhances student record management but also aligns with user needs for better data handling in educational environments. The integration of this feature is crucial for maintaining up-to-date and comprehensive student profiles.