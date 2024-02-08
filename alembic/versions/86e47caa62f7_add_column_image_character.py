"""Add column image Character

Revision ID: 86e47caa62f7
Revises: 82c44154ec5e
Create Date: 2024-02-08 22:29:26.126749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86e47caa62f7'
down_revision: Union[str, None] = '82c44154ec5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('image', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'image')
    # ### end Alembic commands ###
