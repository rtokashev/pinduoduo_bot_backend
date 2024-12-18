"""Убрана уникальность поля joint_purchase_request.chat_id

Revision ID: 8b0411711a52
Revises: d741067358c5
Create Date: 2023-06-21 23:53:48.930716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b0411711a52'
down_revision = 'd741067358c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('joint_purchase_request_chat_id_key', 'joint_purchase_request', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('joint_purchase_request_chat_id_key', 'joint_purchase_request', ['chat_id'])
    # ### end Alembic commands ###
