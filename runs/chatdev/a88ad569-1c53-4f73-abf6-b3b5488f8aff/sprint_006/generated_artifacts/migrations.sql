-- Check if the email column exists before adding it to students
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='students' AND column_name='email') THEN
        ALTER TABLE students ADD COLUMN email TEXT NOT NULL;
    END IF;
END $$;
-- Check if the teacher_id column exists before adding it to courses
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='courses' AND column_name='teacher_id') THEN
        ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
    END IF;
END $$;