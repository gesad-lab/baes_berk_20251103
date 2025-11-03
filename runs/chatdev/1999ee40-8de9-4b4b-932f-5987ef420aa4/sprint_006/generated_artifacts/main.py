'''
Migration script to add Teacher entity and update Course entity.
'''
from sqlalchemy import Column, String, Integer, create_engine, text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from database import init_db  # Importing init_db to ensure database initialization
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Required email field
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Add this line
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
def upgrade():
    '''
    Creates the Course table and creates the Teacher table.
    '''
    with engine.connect() as connection:
        # Create the courses table with teacher_id foreign key
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                level TEXT NOT NULL,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            )
        '''))
        # Create the teachers table
        connection.execute(text('CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)'))
        # Create the association table for the many-to-many relationship
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS student_courses (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
            )
        '''))
def downgrade():
    '''
    Removes the email column from the Student table if needed.
    '''
    # Note: Dropping columns is not supported in SQLite, so this function is left empty.
    pass
if __name__ == "__main__":
    init_db()  # Ensure the database and tables are created first
    upgrade()  # Then run the upgrade to create the Course and Teacher tables