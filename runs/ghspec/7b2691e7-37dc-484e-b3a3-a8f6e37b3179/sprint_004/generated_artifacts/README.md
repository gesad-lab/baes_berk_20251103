# README.md

# Educational Management System

This project provides an educational management system that allows for managing students, courses, and their relationships.

## Setup Instructions

Follow these steps to set up the development environment:

1. **Set Up Environment**: Ensure the virtual environment is active.
2. **Install Dependencies**: Run the following command to install all necessary dependencies:
   ```bash
   pip install Flask SQLAlchemy Marshmallow pytest
   ```

## Database Schema Migration

This application uses Alembic for handling database migrations. 

### Adding Course Relationships

We've introduced a many-to-many relationship structure between students and courses. This is achieved through a junction table called `StudentCourses`.

1. **Migration Script**: The following migration script creates the `StudentCourses` table while preserving existing student and course data:
   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.create_table(
           'student_courses',
           sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
           sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
           sa.PrimaryKeyConstraint('student_id', 'course_id')
       )

   def downgrade():
       op.drop_table('student_courses')
   ```

## API Endpoints

### Student-Course Associations

The following API endpoints have been introduced to manage course associations for students.

1. **Associate Courses with a Student**:

   - **POST** `/students/{studentId}/courses`
   - Description: Associates specified courses with a student.
   - Validation: Each course must exist before association.

2. **Retrieve Courses for a Student**:

   - **GET** `/students/{studentId}/courses`
   - Description: Retrieves a list of courses associated with the specified student.

### Marshmallow Validation

All input and output data for the above endpoints are validated and serialized using Marshmallow schemas.

## Testing

We maintain a high standard for testing to ensure reliability:

- **Unit and Integration Tests**: Tests are implemented for the new student-course association functionality.
- **Coverage**: Our goal is to achieve at least 70% coverage for business logic and 90% for validation routes.

## Documentation Updates

Detailed API documentation has been updated to reflect the new endpoints and usage examples. 

This approach ensures that adding course relationships enhances the educational management system while maintaining existing functionalities. 

## Conclusion

This README serves as a guide to setting up the project, understanding the new features added, and utilizing the API effectively.