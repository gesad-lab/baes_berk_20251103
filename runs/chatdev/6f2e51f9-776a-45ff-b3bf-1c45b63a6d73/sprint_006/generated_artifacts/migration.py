'''
Migration script to add teacher_id column to the Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your new unique revision ID
down_revision = 'previous_revision_id'  # Replace with the actual revision ID of the previous migration
branch_labels = None
depends_on = None
def upgrade():
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    # Create foreign key constraint for teacher_id
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])
def downgrade():
    # Drop foreign key constraint for teacher_id
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    # Drop teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')