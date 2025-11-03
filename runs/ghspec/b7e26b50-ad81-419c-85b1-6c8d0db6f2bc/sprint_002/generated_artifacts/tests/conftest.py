Here is the updated content for the `tests/conftest.py` file, including the documentation for the new API schemas:

```python
"""
conftest.py

This module contains configuration for pytest and is used to define fixtures and hooks.

API Schema Documentation:
==========================

1. **Create Student with Email**
   - **Endpoint**: `POST /students`
   - **Request Body**:
     - `name`: string, required
     - `email`: string, required
   - **Response**:
     - `201 Created` with a JSON message confirming the student has been created, including their ID and email.

   - **Example Request**:
   ```
   POST /students
   {
       "name": "John Doe",
       "email": "johndoe@example.com"
   }
   ```

   - **Example Response**:
   ```
   HTTP/1.1 201 Created
   {
       "message": "Student created successfully.",
       "student": {
           "id": 1,
           "email": "johndoe@example.com"
       }
   }
   ```

2. **Update Student**
   - **Endpoint**: `PUT /students/{id}`
   - **Request Body**:
     - `email`: string, required (to update the existing student's email)
   - **Response**:
     - `200 OK` with a JSON message confirming the email has been updated.

   - **Example Request**:
   ```
   PUT /students/1
   {
       "email": "newemail@example.com"
   }
   ```

   - **Example Response**:
   ```
   HTTP/1.1 200 OK
   {
       "message": "Student email updated successfully."
   }
   ```

3. **Error Handling**
   - If the request does not contain an email, respond with:
     - `400 Bad Request` and a JSON error message stating "Email is required."
   
   - **Example Error Response**:
   ```
   HTTP/1.1 400 Bad Request
   {
       "error": {
           "code": "E001",
           "message": "Email is required."
       }
   }
   ```

"""

# Existing configurations and fixtures can be defined below
# ...
```

This completed file now includes detailed API schema documentation for creating and updating a student with an email. It adheres to the project's coding standards and preserves the structure of the existing `conftest.py` file.