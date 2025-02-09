"""1

Revision ID: 3ab9546feb58
Revises: 
Create Date: 2025-02-04 18:47:38.599240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ab9546feb58'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Task_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('complition_time_start', sa.DateTime(), nullable=True),
    sa.Column('complition_time_end', sa.DateTime(), nullable=True),
    sa.Column('complited', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Task_data_complited'), 'Task_data', ['complited'], unique=False)
    op.create_index(op.f('ix_Task_data_complition_time_end'), 'Task_data', ['complition_time_end'], unique=False)
    op.create_index(op.f('ix_Task_data_complition_time_start'), 'Task_data', ['complition_time_start'], unique=False)
    op.create_index(op.f('ix_Task_data_id'), 'Task_data', ['id'], unique=False)
    op.create_index(op.f('ix_Task_data_name'), 'Task_data', ['name'], unique=False)
    op.create_table('User_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('tasks', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tasks'], ['Task_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_User_data_age'), 'User_data', ['age'], unique=False)
    op.create_index(op.f('ix_User_data_id'), 'User_data', ['id'], unique=False)
    op.create_index(op.f('ix_User_data_name'), 'User_data', ['name'], unique=False)
    op.create_index(op.f('ix_User_data_position'), 'User_data', ['position'], unique=False)
    op.create_index(op.f('ix_User_data_surname'), 'User_data', ['surname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_User_data_surname'), table_name='User_data')
    op.drop_index(op.f('ix_User_data_position'), table_name='User_data')
    op.drop_index(op.f('ix_User_data_name'), table_name='User_data')
    op.drop_index(op.f('ix_User_data_id'), table_name='User_data')
    op.drop_index(op.f('ix_User_data_age'), table_name='User_data')
    op.drop_table('User_data')
    op.drop_index(op.f('ix_Task_data_name'), table_name='Task_data')
    op.drop_index(op.f('ix_Task_data_id'), table_name='Task_data')
    op.drop_index(op.f('ix_Task_data_complition_time_start'), table_name='Task_data')
    op.drop_index(op.f('ix_Task_data_complition_time_end'), table_name='Task_data')
    op.drop_index(op.f('ix_Task_data_complited'), table_name='Task_data')
    op.drop_table('Task_data')
    # ### end Alembic commands ###
