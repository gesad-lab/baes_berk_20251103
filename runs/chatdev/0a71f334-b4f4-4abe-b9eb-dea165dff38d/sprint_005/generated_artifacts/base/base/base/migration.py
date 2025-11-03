'''
Database migration script for adding email field to Student.
'''
# Run these commands in the terminal
alembic revision --autogenerate -m "Add email field to Student"
alembic upgrade head