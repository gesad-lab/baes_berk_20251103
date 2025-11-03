from src.app import db, migrate

def upgrade():
    """Add teacher_id column to courses table as a foreign key referencing teachers table."""
    # Add the teacher_id column to the courses table
    with op.batch_alter_table('courses') as batch_op:
        batch_op.add_column(db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Remove teacher_id column from courses table."""
    # Remove the teacher_id column from the courses table
    with op.batch_alter_table('courses') as batch_op:
        batch_op.drop_column('teacher_id')