Here's the `manual.md` file that provides a detailed user manual for the Course Management software:

```markdown
# Course Management Software

Manage your courses efficiently with our Course Management Software. This application allows users to create and view courses with essential details.

## Main Functions

- **Create Course**: Users can create a new course by providing a name and level.
- **View Courses**: Users can view a list of all created courses.

## Installation Guide

To run the Course Management Software, you need to set up your environment and install the necessary dependencies. Follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage your dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migrations

Before running the application, ensure that the database schema is up to date. Run the migrations with the following command:

```bash
python -m alembic upgrade head
```

### Step 5: Start the Application

Run the application using the following command:

```bash
python main.py
```

The GUI will open, allowing you to manage your courses.

## How to Use the Software

### Creating a Course

1. In the GUI, enter the **Course Name** and **Course Level** in the respective fields.
2. Click the **Create Course** button.
3. If the course is created successfully, a success message will appear. The fields will be cleared for new input.

### Viewing Courses

1. Click the **View Courses** button.
2. A list of all created courses will be displayed in the list box.

## Troubleshooting

- If you encounter any issues while running the application, ensure that all dependencies are installed correctly.
- Make sure the FastAPI server is running on `http://localhost:8000`.
- Check for any error messages in the GUI and address them accordingly.

## Conclusion

This Course Management Software provides a simple interface for managing courses. Feel free to reach out for support or suggestions for new features!

```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring users can effectively utilize the Course Management Software.