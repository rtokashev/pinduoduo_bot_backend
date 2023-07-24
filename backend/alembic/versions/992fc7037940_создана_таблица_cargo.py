"""Создана таблица cargo

Revision ID: 992fc7037940
Revises: c4b5b97d5041
Create Date: 2023-07-25 01:00:48.071763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '992fc7037940'
down_revision = 'c4b5b97d5041'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cargo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['chat_id'], ['users.telegram_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cargo_created_at'), 'cargo', ['created_at'], unique=False)
    op.create_index(op.f('ix_cargo_id'), 'cargo', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cargo_id'), table_name='cargo')
    op.drop_index(op.f('ix_cargo_created_at'), table_name='cargo')
    op.drop_table('cargo')
    # ### end Alembic commands ###
