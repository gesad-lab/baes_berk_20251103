'''
Migration command to add Course table while preserving existing Student data.
'''
alembic revision --autogenerate -m "Add Course table and student_course association"
alembic upgrade head