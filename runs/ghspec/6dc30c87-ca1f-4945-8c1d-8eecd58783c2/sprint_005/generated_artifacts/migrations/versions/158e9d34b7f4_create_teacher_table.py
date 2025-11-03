```python
"""Create teacher table

Revision ID: 158e9d34b7f4
Revises: <previous_revision_id>
Create Date: <current_date>
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

# revision identifiers, used by Alembic.
revision = '158e9d34b7f4'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    """Create the teacher table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True)
    )


def downgrade():
    """Drop the teacher table."""
    op.drop_table('teachers')


def validate_teacher_data(name: str, email: str) -> None:
    """Validate the teacher data before creating the record.

    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Raises:
        ValueError: If the name or email is missing.
    """
    if not name:
        raise ValueError("E001: Name field is required.")
    if not email:
        raise ValueError("E002: Email field is required.")


def create_teacher(name: str, email: str):
    """Create a new teacher in the database.

    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Raises:
        IntegrityError: If the email already exists.
        ValueError: If validation fails.

    Returns:
        int: The ID of the newly created teacher.
    """
    try:
        validate_teacher_data(name, email)

        # Assuming you have a session object to interact with the database
        # Here you'd normally add the teacher record to the session and commit
        teacher = Teacher(name=name, email=email)  # Assuming Teacher is a SQLAlchemy model
        session.add(teacher)
        session.commit()
        
        return teacher.id
    
    except IntegrityError:
        session.rollback()
        raise ValueError("E003: Email must be unique.") from None
```
