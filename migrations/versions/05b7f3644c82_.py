"""empty message

Revision ID: 05b7f3644c82
Revises: 
Create Date: 2017-12-20 14:08:27.257260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05b7f3644c82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hosts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(length=100), nullable=False),
    sa.Column('wip', sa.String(length=100), nullable=False),
    sa.Column('iip', sa.String(length=100), nullable=False),
    sa.Column('idc', sa.String(length=100), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('cat_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['cat_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hostname'),
    sa.UniqueConstraint('idc'),
    sa.UniqueConstraint('iip'),
    sa.UniqueConstraint('wip')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hosts')
    # ### end Alembic commands ###
