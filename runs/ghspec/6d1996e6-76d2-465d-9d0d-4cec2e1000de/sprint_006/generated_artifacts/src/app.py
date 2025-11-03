```python
from models.course import Course
from services.teacher import TeacherService


class CourseService:
    def __init__(self):
        self.courses = {}  # Simulating a database for courses
        self.teacher_service = TeacherService()  # Instantiate teacher service

    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        """Assign a teacher to a specific course."""
        if not self.teacher_service.does_teacher_exist(teacher_id):
            raise ValueError(f'E001: Teacher with ID {teacher_id} does not exist.')

        course = self.courses.get(course_id)
        if course:
            course.teacher_id = teacher_id  # Assign the teacher ID to the course
        else:
            raise ValueError(f'E002: Course with ID {course_id} does not exist.')

    def remove_teacher_from_course(self, course_id: int):
        """Remove the assigned teacher from a specific course."""
        course = self.courses.get(course_id)
        if course:
            course.teacher_id = None  # Set teacher ID to None, effectively removing the assignment
        else:
            raise ValueError(f'E002: Course with ID {course_id} does not exist.')

    def get_course_with_teacher_info(self, course_id: int):
        """Retrieve course details along with assigned teacher's name."""
        course = self.courses.get(course_id)
        if not course:
            raise ValueError(f'E002: Course with ID {course_id} does not exist.')

        teacher_name = self.teacher_service.get_teacher_name(course.teacher_id) if course.teacher_id else None
        return {
            'course_id': course.id,
            'course_name': course.name,
            'teacher_name': teacher_name,
        }
```