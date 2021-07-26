"""Added required tables

Revision ID: ac17695451f0
Revises: 
Create Date: 2021-07-25 11:32:14.248664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac17695451f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('a',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('create_date', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('b',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('b')
    op.drop_table('a')
    # ### end Alembic commands ###
