"""empty message

Revision ID: 14b8bc90ad42
Revises: 1ad22291eb4b
Create Date: 2015-11-27 15:29:47.206000

"""

# revision identifiers, used by Alembic.
revision = '14b8bc90ad42'
down_revision = '1ad22291eb4b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teste',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teste')
    ### end Alembic commands ###