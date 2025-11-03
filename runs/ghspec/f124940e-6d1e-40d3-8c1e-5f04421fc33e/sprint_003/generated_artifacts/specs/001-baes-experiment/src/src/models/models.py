from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(name={self.name}, level={self.level})>"

    def as_dict(self):
        """Convert the Course instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
        }