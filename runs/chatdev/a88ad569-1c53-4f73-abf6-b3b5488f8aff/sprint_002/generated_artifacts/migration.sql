'''
SQL script for migrating the database schema.
'''
ALTER TABLE students ADD COLUMN email TEXT;  -- Allow null values for existing records