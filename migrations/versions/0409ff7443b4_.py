"""empty message

Revision ID: 0409ff7443b4
Revises: 
Create Date: 2021-09-12 23:53:55.411531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0409ff7443b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('folders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=100), nullable=True),
    sa.Column('unit_messure', sa.String(length=30), nullable=True),
    sa.Column('unit_weight', sa.String(length=30), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proyects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('client_name', sa.String(length=100), nullable=True),
    sa.Column('deliver_date', sa.Date(), nullable=True),
    sa.Column('annotations', sa.String(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.Column('total_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_date', sa.String(length=100), nullable=True),
    sa.Column('beg_time', sa.Numeric(), nullable=True),
    sa.Column('current_time', sa.Numeric(), nullable=True),
    sa.Column('final_time', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('hour_price', sa.Numeric(), nullable=True),
    sa.Column('profit', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('times')
    op.drop_table('proyects')
    op.drop_table('materials')
    op.drop_table('folders')
    # ### end Alembic commands ###