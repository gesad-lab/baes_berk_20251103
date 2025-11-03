```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import relationship
from src.database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Optional: Define any relationships here if needed in the future


async def upgrade(database: AsyncSession):
    """Apply the migration to create the teachers table."""
    async with database.begin():
        # Create the teachers table
        await database.run_sync(Base.metadata.create_all)

async def downgrade(database: AsyncSession):
    """Rollback the migration to drop the teachers table."""
    async with database.begin():
        # Drop the teachers table
        await database.run_sync(Base.metadata.drop_all)
```