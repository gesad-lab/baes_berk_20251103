Here's a detailed user manual for the ChatDev Student Application, which includes an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# ChatDev Student Application

The ChatDev Student Application is designed to manage student and course relationships effectively. This application allows students to enroll in multiple courses, providing a robust framework for educational institutions to track student progress and course offerings.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Enrollment**: Students can enroll in multiple courses, and the application maintains a many-to-many relationship between students and courses.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and easy access.

## Quick Install

To set up the ChatDev Student Application, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic
```

## Environment Setup

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd chatdev_student_app
   ```

2. **Install Dependencies**: Use pip to install the necessary packages.

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Initialization**: The application uses SQLite for data storage. The database will be automatically created when you run the application for the first time.

## Usage

1. **Run the Application**: To start the application, execute the following command:

   ```bash
   python main.py
   ```

2. **Access the Dashboard**: Once the application is running, you can access the dashboard through your web browser. The default URL is `http://localhost:8000`.

3. **Managing Students and Courses**:
   - **Add a Student**: Fill in the required fields (name and email) and submit the form.
   - **Add a Course**: Provide the course name and level, then submit.
   - **Enroll Students in Courses**: After creating students and courses, you can enroll students in courses through the dashboard interface.

4. **Database Migration**: The application includes a migration script that ensures existing data is preserved when updating the database schema. This is handled automatically when you run the application.

## Additional Information

For detailed documentation on the API and usage examples, please refer to the following sections:

- **Getting Started**: Learn how to set up the environment and run simple examples.
- **How-To Examples**: Explore demos and integrations to understand how to use the application effectively.
- **Reference**: Access full API documentation for advanced usage.
- **Resources**: Gain insights into core concepts and best practices.

For any issues or support requests, please contact our support team or visit our [support page](#).

Thank you for using the ChatDev Student Application!
```

This manual provides a comprehensive overview of the application, ensuring users can easily install, set up, and utilize its features effectively.