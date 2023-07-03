"""Initial

Revision ID: 60f1d9725e31
Revises: 
Create Date: 2023-06-14 04:25:33.920194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60f1d9725e31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('joint_purchase_request',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('goods_id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.Text(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('post_url', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chat_id'),
    sa.UniqueConstraint('link')
    )
    op.create_index(op.f('ix_joint_purchase_request_created_at'), 'joint_purchase_request', ['created_at'], unique=False)
    op.create_index(op.f('ix_joint_purchase_request_goods_id'), 'joint_purchase_request', ['goods_id'], unique=False)
    op.create_index(op.f('ix_joint_purchase_request_id'), 'joint_purchase_request', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('language_code', sa.String(), nullable=True),
    sa.Column('is_banned', sa.Boolean(), nullable=True),
    sa.Column('is_subscriber', sa.Boolean(), nullable=True),
    sa.Column('subscription_end_date', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('telegram_id'),
    sa.UniqueConstraint('telegram_id', 'phone')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_subscription_end_date'), 'users', ['subscription_end_date'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_subscription_end_date'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_joint_purchase_request_id'), table_name='joint_purchase_request')
    op.drop_index(op.f('ix_joint_purchase_request_goods_id'), table_name='joint_purchase_request')
    op.drop_index(op.f('ix_joint_purchase_request_created_at'), table_name='joint_purchase_request')
    op.drop_table('joint_purchase_request')
    # ### end Alembic commands ###