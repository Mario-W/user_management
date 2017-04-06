"""empty message

Revision ID: e79d45fb58f7
Revises: 
Create Date: 2017-04-02 22:57:30.238894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e79d45fb58f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('姓名', sa.String(length=30), nullable=False),
    sa.Column('年龄', sa.SmallInteger(), nullable=True),
    sa.Column('性别', sa.String(length=2), nullable=False),
    sa.Column('地址', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
