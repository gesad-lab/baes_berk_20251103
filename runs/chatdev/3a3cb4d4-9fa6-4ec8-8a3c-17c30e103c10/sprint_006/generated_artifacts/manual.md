```markdown
# Student Management System

A comprehensive application for managing students, teachers, and courses, allowing for easy interaction and data management.

## Main Functions

- **Add Students**: Users can add new students to the system by providing their name and email.
- **Add Teachers**: Users can add new teachers to the system by providing their name and email.
- **Manage Courses**: Courses can be created and linked to teachers, allowing for a structured learning environment.
- **Student-Teacher Relationship**: Each course can have a designated teacher, establishing a clear relationship between students and their instructors.

## Installation

To set up the Student Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. **Initialize the Database**:
   Run the migration script to create the necessary tables and relationships:
   ```bash
   python migration.py
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing:
   ```bash
   python main.py
   ```

2. **User Interface**:
   - A GUI will open, allowing you to interact with the application.
   - You can add students by entering their name and email, then clicking the "Add Student" button.
   - Similarly, you can add teachers by entering their name and email, then clicking the "Add Teacher" button.

3. **Adding Courses**:
   - To add courses and link them to teachers, you may need to extend the GUI functionality (not covered in this manual).

## Additional Information

For further details on the application, including advanced usage and API documentation, please refer to the code comments and the [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/).

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.

```
