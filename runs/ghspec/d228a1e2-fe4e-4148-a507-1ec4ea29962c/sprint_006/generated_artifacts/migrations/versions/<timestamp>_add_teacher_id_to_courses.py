from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Replace with the appropriate migration identifier if applicable
branch_labels = None
depends_on = None

def upgrade():
    # Add a new column 'teacher_id' to the 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Create a foreign key relationship with the 'teachers' table
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')

def downgrade():
    # Drop the foreign key first
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')

    # Remove the 'teacher_id' column from the 'courses' table
    op.drop_column('courses', 'teacher_id')