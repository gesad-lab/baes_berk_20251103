'''
Migration script to add Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'unique_revision_id_for_course'  # Replace with actual unique revision ID for course
down_revision = 'unique_revision_id_for_email'  # Replace with the actual revision ID from xxxx_add_email_field_to_student.py
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    op.drop_table('courses')