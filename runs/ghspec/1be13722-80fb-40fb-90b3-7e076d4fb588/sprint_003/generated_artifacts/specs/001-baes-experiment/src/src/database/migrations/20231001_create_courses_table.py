from alembic import op
import sqlalchemy as sa

# Migration Script for creating Courses table
def upgrade() -> None:
    # Create the courses table with specified columns and requirements
    op.create_table(
        'courses',  # Table name
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),  # Unique identifier
        sa.Column('name', sa.String(), nullable=False),  # Required field for course name
        sa.Column('level', sa.String(), nullable=False)  # Required field for course level
    )

def downgrade() -> None:
    # Drop the courses table on downgrade
    op.drop_table('courses')