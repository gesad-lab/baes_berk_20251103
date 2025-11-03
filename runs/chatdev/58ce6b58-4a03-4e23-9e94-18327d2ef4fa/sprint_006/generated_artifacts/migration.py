from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Update this with a unique revision identifier
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    # Drop the Teacher table
    op.drop_table('teachers')