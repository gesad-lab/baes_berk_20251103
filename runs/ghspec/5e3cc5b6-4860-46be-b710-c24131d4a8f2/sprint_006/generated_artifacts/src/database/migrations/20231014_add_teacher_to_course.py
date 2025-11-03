from sqlalchemy import Column, Integer, ForeignKey
from database.database import Base

class MigrationAddTeacherToCourse(Base):
    """Migration to add the teacher_id foreign key to the courses table."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Nullable to preserve existing data
    
    # Relationship to access the associated Teacher easily
    teacher = relationship("Teacher", back_populates="courses")  # Assuming a back_populates is defined in the Teacher model

def upgrade():
    """Apply the upgrade: add the teacher_id column to the courses table."""
    with op.batch_alter_table('courses') as batch_op:
        batch_op.add_column(Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """Revert the upgrade: remove the teacher_id column from the courses table."""
    with op.batch_alter_table('courses') as batch_op:
        batch_op.drop_column('teacher_id')