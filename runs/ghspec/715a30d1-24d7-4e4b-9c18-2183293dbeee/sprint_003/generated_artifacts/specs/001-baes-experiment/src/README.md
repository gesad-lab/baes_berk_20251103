# README.md

# Project Title

## Overview

This project is a FastAPI application focused on managing educational entities such as students and courses.

## Setup Instructions

To run the application locally, please follow these steps:

### Prerequisites

Make sure you have the following software installed:

- Python 3.8+
- Poetry (for dependency management)
- SQLite (optional, for testing)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Set up the environment variables. Create a `.env` file based on the `.env.example`, and make sure to include all required configurations.

4. Run the database migrations if applicable (document migrations here if necessary).

### Running the Application

To start the application, use the following command:

```bash
uvicorn main:app --reload
```

### New Course Entity

With the introduction of the Course entity in this sprint, ensure you validate the correct setup of Course-related configurations:

- Update any database tables involved for the Course entity.
- Ensure logging captures any errors related to the new Course functionality.

### Graceful Shutdown

Ensure that the application maintains a graceful shutdown by handling shutdown signals. This will allow the application to close down smoothly, completing any in-flight requests.

## Logging

The application uses logging to capture events, including errors. Ensure to monitor the logs for any unexpected behavior or issues regarding the new Course functionality.

## Testing

Unit tests can be run using pytest. Use the following command to execute the tests:

```bash
pytest
```

Make sure your test database is appropriately configured to avoid conflicts with your production data.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue for any improvements or feature requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.