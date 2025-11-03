```python
from sqlalchemy import Column, Integer, String
from db.database import Base

class AddCourseTable(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)  # Valid values: Beginner, Intermediate, Advanced
```