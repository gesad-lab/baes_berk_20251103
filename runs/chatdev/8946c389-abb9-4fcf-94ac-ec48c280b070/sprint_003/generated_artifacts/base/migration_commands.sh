alembic init alembic
alembic revision --autogenerate -m "Add email field to Student"
alembic upgrade head