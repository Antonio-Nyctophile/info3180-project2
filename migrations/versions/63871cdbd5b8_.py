"""empty message

Revision ID: 63871cdbd5b8
Revises: ee43150ca4e0
Create Date: 2023-04-26 13:35:06.987742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63871cdbd5b8'
down_revision = 'ee43150ca4e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
