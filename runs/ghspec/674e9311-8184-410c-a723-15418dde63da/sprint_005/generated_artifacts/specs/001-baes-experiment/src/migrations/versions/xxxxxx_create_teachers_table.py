from alembic import op
from sqlalchemy import Column, Integer, String

# Define the upgrade function to create the teachers table
def upgrade():
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False, unique=True)
    )

# Define the downgrade function to remove the teachers table
def downgrade():
    op.drop_table('teachers')