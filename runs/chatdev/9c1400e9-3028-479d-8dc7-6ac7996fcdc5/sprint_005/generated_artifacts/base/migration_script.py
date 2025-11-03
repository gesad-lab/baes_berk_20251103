'''
Database migration script to add Course table and email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_and_email_to_student'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Step 1: Add the email column to the students table as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # After ensuring all new records have valid emails, you can later run another migration to make it non-nullable
def downgrade():
    op.drop_table('courses')
    op.drop_column('students', 'email')