from repositories.course_repository import CourseRepository

class CourseService:
    """Contains business logic for managing courses."""
    
    def __init__(self):
        self.course_repo = CourseRepository()

    def create_course(self, name: str, level: str) -> Course:
        """
        Creates a new course.

        :param name: The name of the course.
        :param level: The level of the course.
        :raises ValueError: If course name or level is not provided.
        :return: The created Course object.
        """
        if not name or not level:
            raise ValueError("Course name and level are required.")
        return self.course_repo.create_course(name, level)

    def get_course(self, course_id: int) -> Course:
        """
        Retrieves a course by its ID.

        :param course_id: The ID of the course to retrieve.
        :raises ValueError: If the course is not found.
        :return: The Course object if found.
        """
        course = self.course_repo.get_course_by_id(course_id)
        if not course:
            raise ValueError("Course not found.")
        return course