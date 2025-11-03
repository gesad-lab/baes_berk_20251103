Here's the `manual.md` file that outlines the main functions of the ChatDev application, installation instructions, and usage guidelines:

```markdown
# ChatDev

Changing the digital world through programming

ChatDev is a software application designed to manage students and courses efficiently. It allows users to create and manage student records and course entities with ease.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create and manage courses with specific attributes such as name and level.
- **Database Migration**: Automatically updates the database schema to include new entities while preserving existing data.

## Quick Install

To set up the ChatDev application, you need to install the required dependencies. You can do this using `pip`:

```bash
pip install sqlalchemy pydantic
```

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Environment Setup

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/your-repo/chatdev.git
   cd chatdev
   ```

2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**: 
   To start the application, run:
   ```bash
   python main.py
   ```

## Usage

### Creating a Course

To create a new course, you can use the following schema:

```python
from schemas import CourseCreate
course_data = CourseCreate(name="Mathematics", level="Beginner")
```

### Database Migration

When you run the application, it will automatically create the necessary tables in the SQLite database (`students.db`). The migration process will ensure that existing student data is preserved while adding the new `Course` table.

### Accessing the GUI

The graphical user interface (GUI) is implemented in `gui.py`. You can modify this file to create a user-friendly interface for managing students and courses.

## Documentation

For more detailed information on how to use the ChatDev application, please refer to the following sections:

- **Getting Started**: Installation, setting up the environment, and simple examples.
- **How-To Examples**: Demos, integrations, and helper functions.
- **Reference**: Full API documentation.
- **Resources**: High-level explanations of core concepts.

For any issues or support, please reach out to our support team.

```

This manual provides a comprehensive overview of the ChatDev application, guiding users through installation, setup, and usage while highlighting the main functionalities.