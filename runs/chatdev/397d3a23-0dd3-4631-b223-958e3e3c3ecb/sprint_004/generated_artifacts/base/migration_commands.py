# Install Alembic if not already installed
pip install alembic
# Initialize Alembic in your project
alembic init alembic
# Create a migration script
alembic revision --autogenerate -m "Add Course table"
# Run Migrations
alembic upgrade head