from alembic import op
import sqlalchemy as sa

# Migration to add teacher_id to courses
def upgrade():
    # Start a batch operation on the 'courses' table
    with op.batch_alter_table('courses') as batch_op:
        # Add the new 'teacher_id' column, nullable initially
        batch_op.add_column(sa.Column('teacher_id', sa.Integer(), nullable=True))
        # Create a foreign key relationship with 'teachers' table
        batch_op.create_foreign_key('fk_teacher', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    # Start a batch operation to reverse the changes made in the upgrade
    with op.batch_alter_table('courses') as batch_op:
        # Drop the foreign key constraint
        batch_op.drop_constraint('fk_teacher', 'courses')
        # Remove the 'teacher_id' column
        batch_op.drop_column('teacher_id')