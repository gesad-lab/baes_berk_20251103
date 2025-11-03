'''
Migration script to add Course table while preserving existing Student data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = 'yyyyyy'
branch_labels = None
depends_on = None
def upgrade():
    # Create the Course table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Add teacher_id column with a foreign key constraint
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  # Allow null initially
def downgrade():
    # Drop the Course table
    op.drop_table('courses')