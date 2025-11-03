# README.md

# Student Management Application

This Student Management Application enables management of student records, providing functionalities for creating, retrieving, updating, and deleting student information.

## Application Structure

The project is organized as follows:

```
student-management-app/
    ├── src/
    │   ├── app.py          # Main application entry point
    │   ├── models.py       # Database models (updated to include email)
    │   ├── services.py      # Business logic and API functionalities (updated for validation)
    │   ├── config.py       # Configuration settings
    │   └── database.py     # Database initialization (no changes)
    ├── tests/
    │   ├── test_services.py # Unit tests for service functions (updated for new scenarios)
    ├── requirements.txt     # List of dependencies (no changes)
    ├── .env.example         # Environment variable example
    └── README.md            # Documentation (update to reflect new feature)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management-app.git
   cd student-management-app
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables by copying `.env.example` to `.env` and filling in the necessary details.

## Running the Application

You can run the application using the following command:
```bash
python src/app.py
```

## Running Tests

To ensure everything is functioning correctly, run the unit tests:
```bash
python -m unittest discover -s tests
```

## Features

- Create, read, update, and delete student records.
- Email validation in student records.
- Unit tests covering new scenarios.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements you would like to see.

## License

This project is licensed under the MIT License. See the LICENSE file for details.