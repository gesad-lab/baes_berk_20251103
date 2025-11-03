from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230925_add_email_field'
down_revision = None  # Update as necessary based on the previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Upgrade the database schema to include an email field in the students table."""
    # Add the email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Downgrade the database schema by removing the email field from the students table."""
    # Drop the email column from the students table
    op.drop_column('students', 'email')