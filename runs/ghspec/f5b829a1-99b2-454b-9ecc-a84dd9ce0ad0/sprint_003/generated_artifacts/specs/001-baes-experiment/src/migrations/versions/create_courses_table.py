from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'create_courses_table'
down_revision = None  # Change this if there is a previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Create the courses table in the database."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

def downgrade():
    """Drop the courses table from the database."""
    op.drop_table('courses')