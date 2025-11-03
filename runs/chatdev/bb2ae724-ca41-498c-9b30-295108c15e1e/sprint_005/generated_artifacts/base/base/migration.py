'''
Handles the database migration for adding the Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Check if the 'students' table exists before creating the 'courses' table
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'students' in inspector.get_table_names():
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False)
        )
def downgrade():
    op.drop_table('courses')