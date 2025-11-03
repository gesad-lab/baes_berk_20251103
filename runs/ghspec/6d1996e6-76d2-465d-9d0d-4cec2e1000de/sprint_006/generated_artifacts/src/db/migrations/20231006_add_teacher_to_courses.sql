-- SQL migration script to add teacher_id to courses table
-- This script adds a new column 'teacher_id' to the 'courses' table and updates existing records to have NULL as the default value.

-- Start by adding the new column to the courses table
ALTER TABLE courses 
ADD COLUMN teacher_id INTEGER;

-- Initialize existing records with null values for teacher_id
UPDATE courses 
SET teacher_id = NULL;

-- To maintain data integrity, add a foreign key constraint referencing the teachers table
ALTER TABLE courses 
ADD CONSTRAINT fk_teacher 
FOREIGN KEY (teacher_id) 
REFERENCES teachers(id);