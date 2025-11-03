from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_id_to_courses'
down_revision = None  # Update this with the actual down revision if needed
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to courses table."""
    with op.batch_alter_table('courses') as batch_op:
        # Adding teacher_id column with ForeignKey constraint
        batch_op.add_column(sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """Remove teacher_id column from courses table."""
    with op.batch_alter_table('courses') as batch_op:
        # Dropping teacher_id column
        batch_op.drop_column('teacher_id')