# Install Alembic if not already installed
pip install alembic
# Initialize Alembic in your project
alembic init alembic
# Create a migration script for the Teacher table
alembic revision --autogenerate -m "Create Teacher table"
# Create a migration script for the Course table
alembic revision --autogenerate -m "Add Course table with Teacher relationship"
# Run Migrations
alembic upgrade head