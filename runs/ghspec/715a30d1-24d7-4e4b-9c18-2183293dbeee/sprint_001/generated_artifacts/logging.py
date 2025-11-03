```python
""" 
Logging module for API requests and responses.

This module handles logging of API interactions to provide insight into 
application behavior and issues. It integrates with the FastAPI framework.
 
Project Setup:
1. Create a new Python project.
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required dependencies:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

Running Instructions:
1. Ensure the SQLite database is accessible and schema is created.
2. Start the FastAPI application with the following command:
   ```bash
   uvicorn main:app --reload
   ```
   Replace `main` with the name of your main module where the FastAPI app is defined.

API Endpoints:
1. **Create Student** 
   - **URL**: `/students`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "name": "String"
     }
     ```
   - **Response**: Returns the created student object.
   - **Example Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe"
     }
     ```

2. **Fetch Student by ID**
   - **URL**: `/students/{id}`
   - **Method**: `GET`
   - **Response**: Returns the student object for the provided ID.
   - **Error Response**: 
     - If the student with the provided ID does not exist:
     ```json
     {
       "error": {
         "code": "E404",
         "message": "Student not found."
       }
     }
     ```
"""

import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_request(request):
    """Log incoming requests for monitoring."""
    logging.info(f"Received request: {request.method} {request.url}")

def log_response(response):
    """Log outgoing responses for tracking."""
    logging.info(f"Sending response: {response.status_code} - {response.body if hasattr(response, 'body') else ''}")
```