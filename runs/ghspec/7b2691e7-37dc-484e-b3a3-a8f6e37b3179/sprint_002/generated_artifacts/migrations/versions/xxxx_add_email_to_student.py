```python
# migrations/versions/xxxx_add_email_to_student.py

from alembic import op
import sqlalchemy as sa
from marshmallow import Schema, fields, ValidationError, validates
import re

# revision identifiers, used by Alembic.
revision = 'xxxx_add_email_to_student'
down_revision = None  # Update if you have a previous migration
branch_labels = None
depends_on = None

def validate_email(email):
    """Validate the format of the email."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError('Invalid email format.')

class StudentSchema(Schema):
    """Schema to validate student data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=False, validate=validate_email)  # Email is not mandatory

@op.add_column('student', sa.Column('email', sa.String(length=255), nullable=True))
def upgrade():
    """Apply the migration to add the 'email' column to the 'student' table."""
    pass

def downgrade():
    """Remove the 'email' column from the 'student' table."""
    op.drop_column('student', 'email')
```