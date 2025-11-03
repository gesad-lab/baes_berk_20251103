```python
from alembic import op
import sqlalchemy as sa


def upgrade():
    # Create the teachers table with required columns
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )


def downgrade():
    # Drop the teachers table if it exists
    op.drop_table('teachers')


def update_teacher(teacher_id: int, data: dict) -> dict:
    """
    Update the teacher's information in the database.
    
    Parameters:
    - teacher_id: Unique identifier of the teacher.
    - data: Dictionary containing updated values for `name` and/or `email`.
    
    Returns:
    - JSON response with updated teacher details or error message.
    
    Raises:
    - ValueError: If the provided `email` format is invalid or if the teacher is not found.
    """
    from src.models import Teacher  # Import Teacher model

    # Validate the email format if provided
    if 'email' in data:
        if not isinstance(data['email'], str) or '@' not in data['email']:
            raise ValueError("Invalid email format.")

    # Fetch the teacher record from the database
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404

    # Update the teacher's information
    for key, value in data.items():
        if hasattr(teacher, key) and value is not None:
            setattr(teacher, key, value)

    # Commit the changes to the database
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Email already in use."}}), 400

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```