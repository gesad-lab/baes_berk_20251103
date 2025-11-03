```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional


class Student(BaseModel):
    id: Optional[int] = Field(default=None, description="The ID of the student.")
    name: str = Field(..., description="The name of the student.")

    @validator('name')
    def validate_name(cls, value):
        if not value:
            raise ValueError("Name field is required.")
        return value


class StudentValidation:
    @staticmethod
    def validate_student_data(student_data: dict) -> Student:
        """
        Validate and create a Student instance from the provided data.
        
        Args:
            student_data (dict): Raw student data received in the request.

        Returns:
            Student: A validated Student instance.

        Raises:
            ValueError: If validation fails.
        """
        return Student(**student_data)

    @staticmethod
    def extract_students_list(student_records: List[dict]) -> List[Student]:
        """
        Convert a list of raw student records to a list of Student instances.
        
        Args:
            student_records (List[dict]): Raw student records from the database.

        Returns:
            List[Student]: A list of validated Student instances.
        """
        return [Student(**record) for record in student_records]

```