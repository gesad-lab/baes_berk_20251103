from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the courses table with required fields
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    # Drop the courses table if exists
    op.drop_table('courses')