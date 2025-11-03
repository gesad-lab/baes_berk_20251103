'''
Migration command to add Teacher table while preserving existing Student and Course data.
'''
alembic revision --autogenerate -m "Add Teacher table"
alembic upgrade head