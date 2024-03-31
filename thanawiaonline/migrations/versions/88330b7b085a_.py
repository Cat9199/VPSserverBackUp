"""empty message

Revision ID: 88330b7b085a
Revises: 6bdfc6142f93
Create Date: 2024-01-07 16:56:03.936171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88330b7b085a'
down_revision = '6bdfc6142f93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Ltype', sa.String(length=50), nullable=False))
        batch_op.drop_column('type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=50), nullable=False))
        batch_op.drop_column('Ltype')

    # ### end Alembic commands ###
