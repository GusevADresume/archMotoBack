"""arouselAddClmn2

Revision ID: c134e474ccac
Revises: 
Create Date: 2023-10-09 00:48:57.219752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c134e474ccac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('text_and_img_carousel', sa.Column('header_text', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('text_and_img_carousel', 'header_text')
    # ### end Alembic commands ###
