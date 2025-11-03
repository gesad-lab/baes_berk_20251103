# README.md

## Migration Guide

### Creating the `student_courses` Table

To establish a many-to-many relationship between the `Student` and `Course` entities, you need to run the migration that creates the `student_courses` junction table. This table will facilitate the association of multiple courses to students and vice versa. Follow the steps below:

1. **Run Migration**: Use the following command to execute the migration script that creates the `student_courses` table:

   ```bash
   python migrations.py
   ```

   This command will establish the necessary relationships in the database without altering existing `Student` and `Course` data.

2. **Migration Contents**: The migration will create the `student_courses` table structured as follows:

   ```sql
   CREATE TABLE student_courses (
       student_id INTEGER,
       course_id INTEGER,
       PRIMARY KEY (student_id, course_id),
       FOREIGN KEY(student_id) REFERENCES students(id),
       FOREIGN KEY(course_id) REFERENCES courses(id)
   );
   ```

3. **Testing the Migration**: After running the migration, it's recommended to validate that the table was created successfully and can be utilized by running existing tests or creating new tests in the `tests/test_courses.py` file.

4. **Endpoints for Course Associations**:
   - **Associate a Course with a Student**: Post to `/students/{student_id}/courses` with JSON containing the course ID.
   - **Retrieve Courses for a Student**: Get from `/students/{student_id}/courses` to retrieve associated course details.

### Notes

- Ensure that your database is correctly configured and accessible before running the migration.
- Review the migration function in `migrations.py` for any necessary adjustments to the connection string or execution context.