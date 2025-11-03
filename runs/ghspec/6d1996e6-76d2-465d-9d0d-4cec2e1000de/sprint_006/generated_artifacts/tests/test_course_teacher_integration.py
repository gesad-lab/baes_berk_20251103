```python
import unittest
from unittest.mock import patch
from services.course import CourseService
from models.course import Course
from models.teacher import Teacher

class TestCourseService(unittest.TestCase):
    def setUp(self):
        """Set up a test environment for Course tests."""
        self.course_service = CourseService()
        self.course_id = 1  # Example course ID
        self.teacher_id = 1  # Example teacher ID
        self.non_existent_teacher_id = 999  # An ID that does not exist

    @patch('models.course.Course')
    @patch('models.teacher.Teacher')
    def test_assign_teacher_to_course_success(self, mock_teacher, mock_course):
        """Test assigning a teacher to a course successfully."""
        mock_course.get.return_value = Course(id=self.course_id, teacher_id=None)
        mock_teacher.get.return_value = Teacher(id=self.teacher_id)

        result = self.course_service.assign_teacher_to_course(self.course_id, self.teacher_id)
        self.assertEqual(result.teacher_id, self.teacher_id)
        mock_course.get.assert_called_with(self.course_id)
        mock_teacher.get.assert_called_with(self.teacher_id)

    @patch('models.course.Course')
    def test_retrieve_course_with_teacher_info(self, mock_course):
        """Test retrieving course details with associated teacher information."""
        mock_course.get.return_value = Course(id=self.course_id, teacher_id=self.teacher_id)

        course_details = self.course_service.get_course_with_teacher(self.course_id)
        self.assertEqual(course_details.teacher_id, self.teacher_id)
        mock_course.get.assert_called_with(self.course_id)

    @patch('models.course.Course')
    def test_remove_teacher_from_course_success(self, mock_course):
        """Test removing a teacher assignment from a course successfully."""
        mock_course.get.return_value = Course(id=self.course_id, teacher_id=self.teacher_id)

        result = self.course_service.remove_teacher_from_course(self.course_id)
        self.assertIsNone(result.teacher_id)
        mock_course.get.assert_called_with(self.course_id)

    @patch('models.teacher.Teacher')
    def test_assign_non_existent_teacher(self, mock_teacher):
        """Test error handling for assigning a non-existent teacher to a course."""
        mock_teacher.get.side_effect = Exception("Teacher does not exist")

        with self.assertRaises(Exception) as context:
            self.course_service.assign_teacher_to_course(self.course_id, self.non_existent_teacher_id)

        self.assertEqual(str(context.exception), "Teacher does not exist")
        mock_teacher.get.assert_called_with(self.non_existent_teacher_id)

if __name__ == '__main__':
    unittest.main()
```