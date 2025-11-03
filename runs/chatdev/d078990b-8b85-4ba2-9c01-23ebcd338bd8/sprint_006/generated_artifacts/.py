'''
Alembic migration script to add teacher relationship to Course entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema.
    '''
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])
def downgrade():
    '''
    Downgrade the database schema.
    '''
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')