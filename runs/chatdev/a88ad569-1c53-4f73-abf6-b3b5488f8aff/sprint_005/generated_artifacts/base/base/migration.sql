'''
SQL script for database migration.
'''
ALTER TABLE students ADD COLUMN email TEXT NOT NULL;