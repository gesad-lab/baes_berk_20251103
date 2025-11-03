from models.course import Course
from database import session

class CourseRepository:
    """Handles database interactions for the Course entity."""
    
    def create_course(self, name: str, level: str) -> Course:
        """
        Create a new course in the database.
        
        Parameters:
            name (str): The name of the course.
            level (str): The level of the course.
        
        Returns:
            Course: The created Course object.
        
        Raises:
            ValueError: If the name or level is empty.
        """
        if not name or not level:
            raise ValueError("Course name and level are required.")
        
        # Create a new Course instance
        course = Course(name=name, level=level)
        
        # Add the course to the session and commit to the database
        session.add(course)
        session.commit()
        
        return course

    def get_course_by_id(self, course_id: int) -> Course:
        """
        Retrieve a course by its ID from the database.
        
        Parameters:
            course_id (int): The ID of the course to retrieve.
        
        Returns:
            Course: The Course object with the specified ID.
        
        Raises:
            ValueError: If the course does not exist.
        """
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            raise ValueError("Course not found.")
        
        return course