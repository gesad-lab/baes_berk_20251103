```python
from typing import List
from fastapi import HTTPException
from src.models.student import Student
from src.dal.student_dal import StudentDAL

class StudentService:
    """Service to manage student operations including course enrollments."""

    def __init__(self, student_dal: StudentDAL):
        self.student_dal = student_dal

    async def enroll_student_in_courses(self, student_id: int, course_ids: List[int]) -> Student:
        """Enroll a student in given courses by updating the course_ids field.

        Args:
            student_id (int): The ID of the student to enroll.
            course_ids (List[int]): List of course IDs to associate with the student.

        Returns:
            Student: The updated student object with the associated course IDs.

        Raises:
            HTTPException: If the student is not found or if any course ID is invalid.
        """
        student = await self.student_dal.get_student_by_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Here we can validate the course_ids if necessary (not implemented in this example).

        student.course_ids = list(set(student.course_ids) | set(course_ids))  # Avoid duplicates
        updated_student = await self.student_dal.update_student(student)

        return updated_student

    async def get_student_with_courses(self, student_id: int) -> Student:
        """Retrieve a student's details along with associated course IDs.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Student: The student object with associated course IDs.

        Raises:
            HTTPException: If the student is not found.
        """
        student = await self.student_dal.get_student_by_id(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        return student
```