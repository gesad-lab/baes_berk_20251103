from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base  # Assuming there's a base model to inherit from

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Establish a many-to-many relationship with StudentCourse
    students = relationship("StudentCourse", back_populates="course")  # Link to the junction table

# Ensure that the rest of the existing Course model code remains intact
# (Add other existing fields and methods as necessary)

# Note: You should also ensure that the corresponding import statements and other parts of the application
# are updated to accommodate this new relationship, particularly in the Student model.