"""empty message

Revision ID: 3db8d3c612d7
Revises: 14b8bc90ad42
Create Date: 2015-11-28 23:18:26.164000

"""

# revision identifiers, used by Alembic.
revision = '3db8d3c612d7'
down_revision = '14b8bc90ad42'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teste', sa.Column('image', sa.LargeBinary(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teste', 'image')
    ### end Alembic commands ###