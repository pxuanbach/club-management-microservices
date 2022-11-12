"""remove username

Revision ID: 00520973a73f
Revises: 03c6d6975609
Create Date: 2022-11-11 16:13:07.474867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00520973a73f'
down_revision = '03c6d6975609'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_username', table_name='users')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    # ### end Alembic commands ###
