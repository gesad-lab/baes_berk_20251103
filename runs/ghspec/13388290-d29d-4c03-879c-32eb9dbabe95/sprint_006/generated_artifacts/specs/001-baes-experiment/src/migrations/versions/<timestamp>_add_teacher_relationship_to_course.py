from flask_migrate import op
import sqlalchemy as sa

def upgrade():
    # Add a new column 'teacher_id' to 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    # Create foreign key relationship with the 'teachers' table
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    # Remove the 'teacher_id' column from the 'courses' table
    op.drop_column('courses', 'teacher_id')