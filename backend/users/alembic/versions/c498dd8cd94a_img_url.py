"""img_url

Revision ID: c498dd8cd94a
Revises: f53f1feb5506
Create Date: 2022-11-08 11:04:22.330019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c498dd8cd94a'
down_revision = 'f53f1feb5506'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('img_url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'img_url')
    # ### end Alembic commands ###
