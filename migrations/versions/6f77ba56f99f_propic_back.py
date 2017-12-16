"""propic back

Revision ID: 6f77ba56f99f
Revises: 997647e3ee38
Create Date: 2017-12-12 13:02:49.134588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f77ba56f99f'
down_revision = '997647e3ee38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pro_pic', sa.LargeBinary(), nullable=True))
    op.create_unique_constraint(None, 'users', ['pro_pic'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'pro_pic')
    # ### end Alembic commands ###
