from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add the 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, unique=True))

def downgrade():
    # Remove the 'email' column from the 'students' table
    op.drop_column('students', 'email')