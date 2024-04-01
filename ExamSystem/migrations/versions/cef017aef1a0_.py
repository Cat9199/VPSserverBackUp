"""empty message

Revision ID: cef017aef1a0
Revises: f8e722349ca7
Create Date: 2024-03-10 13:22:46.022087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cef017aef1a0'
down_revision = 'f8e722349ca7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mcq_answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imgWithAnswer', sa.String(length=120), nullable=True))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imgWithQuestions', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('imgWithQuestions')

    with op.batch_alter_table('mcq_answer', schema=None) as batch_op:
        batch_op.drop_column('imgWithAnswer')

    # ### end Alembic commands ###