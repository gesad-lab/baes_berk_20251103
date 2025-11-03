'''
Run Alembic migrations.
'''
# Ensure to create a migration script for the Teacher table
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))  # Add this line
def downgrade():
    op.drop_column('courses', 'teacher_id')  # Add this line to drop the column
    op.drop_table('teachers')