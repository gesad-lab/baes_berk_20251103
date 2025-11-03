from models.student_courses import StudentCourses
from models.student import Student
from models.course import Course
from database import session

class StudentCoursesRepository:
    """Handles database interactions for Student-Course relationships."""
    
    def enroll_student_in_course(self, student_id: int, course_id: int) -> None:
        """Enrolls a student in a specific course.

        Args:
            student_id (int): The ID of the student to enroll.
            course_id (int): The ID of the course to enroll the student in.

        Raises:
            ValueError: If the student or course does not exist.
            Exception: If there is an error while enrolling the student.
        """
        try:
            # Check if student and course exist
            student = session.query(Student).get(student_id)
            course = session.query(Course).get(course_id)
            if not student:
                raise ValueError(f"Student with ID {student_id} does not exist.")
            if not course:
                raise ValueError(f"Course with ID {course_id} does not exist.")
            
            # Create a new enrollment record
            enrollment = StudentCourses(student_id=student_id, course_id=course_id)
            session.add(enrollment)
            session.commit()
        except Exception as e:
            # Rollback in case of error
            session.rollback()
            raise Exception(f"An error occurred while enrolling student: {str(e)}") from e
        
    def remove_student_from_course(self, student_id: int, course_id: int) -> None:
        """Removes a student from a specific course.

        Args:
            student_id (int): The ID of the student to remove.
            course_id (int): The ID of the course to remove the student from.

        Raises:
            ValueError: If the student-course relationship does not exist.
            Exception: If there is an error while removing the student.
        """
        try:
            # Fetch the enrollment record to delete
            enrollment = session.query(StudentCourses).filter_by(student_id=student_id, course_id=course_id).first()
            if not enrollment:
                raise ValueError(f"Student with ID {student_id} is not enrolled in course ID {course_id}.")
            
            session.delete(enrollment)
            session.commit()
        except Exception as e:
            # Rollback in case of error
            session.rollback()
            raise Exception(f"An error occurred while removing student from course: {str(e)}") from e
    
    def get_courses_for_student(self, student_id: int):
        """Retrieves all courses for a specific student.

        Args:
            student_id (int): The ID of the student to retrieve courses for.

        Returns:
            list: A list of courses that the student is enrolled in.

        Raises:
            ValueError: If the student does not exist.
        """
        student = session.query(Student).get(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        
        # Return the associated courses through the join table
        return student.courses

    def get_students_in_course(self, course_id: int):
        """Retrieves all students enrolled in a specific course.

        Args:
            course_id (int): The ID of the course to retrieve students for.

        Returns:
            list: A list of students enrolled in the course.

        Raises:
            ValueError: If the course does not exist.
        """
        course = session.query(Course).get(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")
        
        # Return the associated students through the join table
        return course.students