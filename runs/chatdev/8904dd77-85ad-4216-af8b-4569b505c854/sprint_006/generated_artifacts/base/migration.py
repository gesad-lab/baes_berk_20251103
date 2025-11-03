'''
Database migration script to add Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Check for existing data in students and courses
    # (This is a placeholder for any checks you may want to implement)
    # Step 2: Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Step 3: Ensure existing data in students and courses is preserved
    # (This step is typically handled by the database itself, but you may want to ensure that no constraints are violated.)
def downgrade():
    # Step 4: Drop the teachers table during downgrade
    op.drop_table('teachers')