'''
Migration script to add email field to Student entity and create Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('courses')
    op.drop_column('students', 'email')