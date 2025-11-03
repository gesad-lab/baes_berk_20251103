from models.course import Course
from database import session

class CourseRepository:
    """Handles database interactions for Course entity."""

    def assign_teacher(self, course_id: int, teacher_id: int) -> Course:
        """Assign a teacher to a course by updating the course's teacher_id.

        Args:
            course_id (int): The ID of the course to update.
            teacher_id (int): The ID of the teacher to assign to the course.

        Returns:
            Course: The updated course object.

        Raises:
            ValueError: If the course does not exist.
        """
        # Fetch the course by its id
        course = session.query(Course).filter_by(id=course_id).first()
        
        if not course:
            raise ValueError(f'Course with ID {course_id} does not exist.')  # Fail fast with a clear message
        
        # Assign the teacher to the course
        course.teacher_id = teacher_id
        
        # Commit changes to the database
        session.commit()
        
        return course  # Return the updated course object

    # Additional methods for the CourseRepository can be added here as needed.