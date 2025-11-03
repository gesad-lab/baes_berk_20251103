# README.md

# Project Title

A brief description of what this project does and who it's for.

## Teacher Functionality

This project has been updated to include a new **Teacher** functionality that allows for the management of teachers and their associated courses. The functionality enables operations such as adding new teachers, updating existing teacher information, and retrieving the list of teachers.

### API Interactions

The following endpoints have been introduced to facilitate interactions with the Teacher functionality:

- **GET /api/v1/teachers**
  - Retrieves a list of all teachers.
  - **Response**: 
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "courses": [1, 2]
      },
      ...
    ]
    ```

- **POST /api/v1/teachers**
  - Adds a new teacher.
  - **Request Body**:
    ```json
    {
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
    ```
  - **Response**: 
    ```json
    {
      "id": 2,
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
    ```

- **PUT /api/v1/teachers/{id}**
  - Updates an existing teacher's information.
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "janesmith@example.com"
    }
    ```
  - **Response**: 
    ```json
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "janesmith@example.com"
    }
    ```

- **DELETE /api/v1/teachers/{id}**
  - Deletes a teacher by their ID.
  - **Response**: 
    ```json
    {
      "message": "Teacher deleted successfully."
    }
    ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Change to the project directory:
   ```bash
   cd your_repository
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, use:
```bash
flask run
```

## Running Tests

To run the tests, execute:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.