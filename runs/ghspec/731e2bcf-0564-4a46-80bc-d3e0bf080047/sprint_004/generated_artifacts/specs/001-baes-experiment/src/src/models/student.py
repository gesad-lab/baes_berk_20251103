```python
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    course_ids = db.Column(db.Text, nullable=True)  # New field to hold course IDs as a string

    @property
    def course_ids_list(self):
        """Returns a list of course IDs for the student."""
        return [int(course_id) for course_id in self.course_ids.split(",")] if self.course_ids else []

    @course_ids_list.setter
    def course_ids_list(self, course_ids):
        """Sets the course_ids field from a list of course IDs."""
        self.course_ids = ",".join(map(str, course_ids))  # Store course IDs as a comma-separated string
```