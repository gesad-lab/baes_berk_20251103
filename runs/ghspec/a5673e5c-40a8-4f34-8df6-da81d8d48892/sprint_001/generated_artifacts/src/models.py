```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all SQLAlchemy models
Base = declarative_base()

class User(Base):
    """
    User model for storing user information in the database.
    
    Attributes:
        id (int): The primary key for the user, auto-incremented.
        username (str): The unique username for the user.
        email (str): The unique email address of the user.
        password_hash (str): The hashed password for the user.
    """
    __tablename__ = 'users'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Item(Base):
    """
    Item model for storing item information in the database.

    Attributes:
        id (int): The primary key for the item, auto-incremented.
        owner_id (int): The foreign key referencing the owner (User).
        name (str): The name of the item.
        description (str): A brief description of the item.
    """
    __tablename__ = 'items'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, nullable=False)  # Assume foreign key setup will be handled in API logic
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

# You may add additional models as required...
```