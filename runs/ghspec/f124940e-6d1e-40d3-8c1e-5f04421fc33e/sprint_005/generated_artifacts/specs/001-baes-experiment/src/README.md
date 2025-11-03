# README.md

# GHSpec-Kit Project

## Overview

This project serves as a template for experiments utilizing GHSpec-Kit, implementing a FastAPI application that provides a course enrollment system. The goal of this project is to help developers understand and implement features and enhancements.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- FastAPI
- SQLAlchemy (or your choice of ORM)
- pytest for testing

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ghspec-kit.git
   cd ghspec-kit
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

Add your configuration to the `.env` file. A template is available as `.env.example`.

### Running the Application

To run the FastAPI application, use:
```
uvicorn src.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to access the auto-generated API documentation.

### Running Tests

To run the tests, use:
```
pytest
```
Ensure that your test database is set up correctly before running tests.

## Features

- Create courses
- Enroll students in courses
- View enrolled students for a course

## Directory Structure

```
.
├── src
│   ├── main.py                # FastAPI application instance
│   ├── models                  # Database models (e.g., Course)
│   └── services                # Business logic (e.g., enrollment services)
└── tests                       # Test cases for APIs and services
```

## Contribution

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is built with contributions from the community and is inspired by various open-source frameworks and libraries.