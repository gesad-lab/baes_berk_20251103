# Example Requests for Student API

## Setup
To run this application, ensure you have the necessary dependencies installed. Follow the instructions below to set up your environment:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and set your configuration variables.

## API Usage

### 1. Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```
- **Example Response**:
   ```json
   {
     "id": 1,
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```

### 2. Retrieve All Students
- **Endpoint**: `GET /students`
- **Example Response**:
   ```json
   [
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     },
     {
       "id": 2,
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
   ]
   ```

### 3. Retrieve Specific Student
- **Endpoint**: `GET /students/1`
- **Example Response**:
   ```json
   {
     "id": 1,
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```

### 4. Update Student
- **Endpoint**: `PUT /students/1`
- **Request Body**:
   ```json
   {
     "name": "John Doe Updated",
     "email": "john.doe.updated@example.com"
   }
   ```
- **Example Response**:
   ```json
   {
     "id": 1,
     "name": "John Doe Updated",
     "email": "john.doe.updated@example.com"
   }
   ```

### 5. Database Migration
- Ensure that the existing `Students` table has been updated to include the `email` field. Existing student records must be preserved throughout this operation.