# README.md

# Development Setup

## Prerequisites
- Python 3.6 or higher
- Virtual environment (recommended)

## Installation Instructions

1. **Set Up the Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Required Packages:**
   Install Flask and Flask-SQLAlchemy using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

3. **Add to requirements.txt:**
   Make sure `requirements.txt` is updated with the following dependencies:
   ```
   Flask==2.0.3
   Flask-SQLAlchemy==2.5.1
   ```

## Running the Application
To run the Flask application, execute:
```bash
flask run
```

## Summary
This project is built using Flask and SQLite to manage entities such as Teachers, Students, and Courses, laying a foundation for future enhancements while maintaining scalability and integration capabilities.