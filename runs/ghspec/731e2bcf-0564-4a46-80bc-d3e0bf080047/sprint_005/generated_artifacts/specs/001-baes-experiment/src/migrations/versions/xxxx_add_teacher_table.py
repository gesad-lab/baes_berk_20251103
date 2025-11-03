from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_table'
down_revision = None  # Adjust this to the previous migration if applicable
branch_labels = None
depends_on = None


def upgrade():
    """Create the Teacher table in the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
    )


def downgrade():
    """Drop the Teacher table in the database."""
    op.drop_table('teachers')