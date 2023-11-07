"""all tables

Revision ID: 0b3b279f0c51
Revises: 
Create Date: 2023-11-02 14:23:55.213672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b3b279f0c51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)

    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=128), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_expense_item'), ['item'], unique=False)
        batch_op.create_index(batch_op.f('ix_expense_timestamp'), ['timestamp'], unique=False)

    op.create_table('income',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=128), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_income_source'), ['source'], unique=False)
        batch_op.create_index(batch_op.f('ix_income_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_income_timestamp'))
        batch_op.drop_index(batch_op.f('ix_income_source'))

    op.drop_table('income')
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_expense_timestamp'))
        batch_op.drop_index(batch_op.f('ix_expense_item'))

    op.drop_table('expense')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
