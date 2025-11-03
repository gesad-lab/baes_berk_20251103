from pydantic import BaseModel, EmailStr, constr, conint
from typing import List, Optional


class UserBase(BaseModel):
    """Base model for the user schema, containing shared fields."""
    username: constr(min_length=3, max_length=50)  # Username must be between 3 and 50 characters
    email: EmailStr  # Email must be a valid email format


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: constr(min_length=8)  # Password must be at least 8 characters


class UserResponse(UserBase):
    """Schema for the user response, including an id."""
    id: conint(ge=1)  # ID must be a positive integer

    class Config:
        orm_mode = True  # Enable ORM mode to serialize ORM objects


class ItemBase(BaseModel):
    """Base model for item schema."""
    name: constr(min_length=1, max_length=100)  # Item name must be between 1 and 100 characters
    description: Optional[str] = None  # Item description is optional


class ItemCreate(ItemBase):
    """Schema for creating a new item."""


class ItemResponse(ItemBase):
    """Schema for the item response, including an id."""
    id: conint(ge=1)  # ID must be a positive integer

    class Config:
        orm_mode = True  # Enable ORM mode to serialize ORM objects


class UserItemsResponse(UserResponse):
    """Schema for user response including related items."""
    items: List[ItemResponse] = []  # Users can have a list of items associated with them
   
    class Config:
        orm_mode = True  # Enable ORM mode to serialize ORM objects