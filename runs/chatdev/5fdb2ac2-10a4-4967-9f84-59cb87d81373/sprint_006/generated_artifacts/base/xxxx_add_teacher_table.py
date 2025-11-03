'''
Migration script to add Teacher table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_table'
down_revision = 'xxxx_add_course_table'  # Ensure this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('teachers')