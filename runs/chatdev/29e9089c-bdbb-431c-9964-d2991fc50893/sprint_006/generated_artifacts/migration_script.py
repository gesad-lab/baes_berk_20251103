'''
Alembic migration script to add Teacher table and preserve existing Student and Course data.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Create Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Step 2: Add teacher_id column to Course table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    op.drop_column('courses', 'teacher_id')
    op.drop_table('teachers')