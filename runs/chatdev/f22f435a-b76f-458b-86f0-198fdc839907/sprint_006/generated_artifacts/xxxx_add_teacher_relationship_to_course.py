'''
Migration script to add teacher relationship to Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  # Set nullable to True
def downgrade():
    op.drop_column('courses', 'teacher_id')  # Remove teacher_id column