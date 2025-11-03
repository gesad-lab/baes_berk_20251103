# Create a new migration script using Alembic
# alembic revision -m "Add email field to students"
# In the migration script, you would add:
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    op.drop_column('students', 'email')