'''
Migration command to add Course table while preserving existing Student data.
'''
alembic revision --autogenerate -m "Add Course table"
alembic upgrade head