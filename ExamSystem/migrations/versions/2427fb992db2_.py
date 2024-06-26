"""empty message

Revision ID: 2427fb992db2
Revises: cef017aef1a0
Create Date: 2024-03-19 12:40:16.192910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2427fb992db2'
down_revision = 'cef017aef1a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_start_date',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('examCode', sa.String(length=120), nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_start_date')
    # ### end Alembic commands ###
