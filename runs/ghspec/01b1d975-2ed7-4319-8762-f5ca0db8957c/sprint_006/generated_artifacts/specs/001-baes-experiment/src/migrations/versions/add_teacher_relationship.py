from alembic import op
import sqlalchemy as sa


def upgrade():
    """Add the teacher_id foreign key to the courses table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Remove the teacher_id foreign key from the courses table."""
    op.drop_column('courses', 'teacher_id')