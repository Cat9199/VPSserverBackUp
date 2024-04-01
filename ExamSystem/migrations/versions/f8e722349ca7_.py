"""empty message

Revision ID: f8e722349ca7
Revises: 2b78706cf6fa
Create Date: 2024-03-09 16:37:51.040705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8e722349ca7'
down_revision = '2b78706cf6fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('examCode', sa.String(length=120), nullable=False),
    sa.Column('questionCode', sa.String(length=120), nullable=False),
    sa.Column('UserAnswers', sa.String(length=120), nullable=False),
    sa.Column('ActualAnswer', sa.String(length=120), nullable=False),
    sa.Column('isTrue', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_marks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('platform', sa.String(length=120), nullable=False),
    sa.Column('userPhone', sa.String(length=120), nullable=False),
    sa.Column('userParentPhone', sa.String(length=120), nullable=False),
    sa.Column('examCode', sa.String(length=120), nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('questionMark', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('questionMark')

    op.drop_table('users_marks')
    op.drop_table('user_answers')
    # ### end Alembic commands ###