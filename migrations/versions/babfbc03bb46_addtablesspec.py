"""addTablesSpec

Revision ID: babfbc03bb46
Revises: 17698330f951
Create Date: 2023-10-11 00:16:25.775110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'babfbc03bb46'
down_revision: Union[str, None] = '17698330f951'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gallery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('page', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('keySpec',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Displacement (cc)', sa.String(), nullable=False),
    sa.Column('Dry Weight (lbs.)', sa.String(), nullable=False),
    sa.Column('Torque (ftlb @ RPM)', sa.String(), nullable=False),
    sa.Column('Tank Capacity (Gallons US)', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('specData',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Engine', sa.String(), nullable=False),
    sa.Column('Displacement', sa.String(), nullable=False),
    sa.Column('Drivetrain', sa.String(), nullable=False),
    sa.Column('Chassis', sa.String(), nullable=False),
    sa.Column('FrontSuspension', sa.String(), nullable=False),
    sa.Column('RearSuspension', sa.String(), nullable=False),
    sa.Column('FrontBrakes', sa.String(), nullable=False),
    sa.Column('RearBrakes', sa.String(), nullable=False),
    sa.Column('ABS', sa.String(), nullable=False),
    sa.Column('FrontWheel', sa.String(), nullable=False),
    sa.Column('RearWheel', sa.String(), nullable=False),
    sa.Column('FrontTire', sa.String(), nullable=False),
    sa.Column('FootControls', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('established', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_constraint('established_established_id_fkey', 'established', type_='foreignkey')
    op.drop_column('established', 'established_id')
    op.add_column('fan', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_constraint('fan_fan_id_fkey', 'fan', type_='foreignkey')
    op.drop_column('fan', 'fan_id')
    op.add_column('interested', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_constraint('interested_contact_id_fkey', 'interested', type_='foreignkey')
    op.drop_column('interested', 'contact_id')
    op.add_column('represent', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_constraint('represent_represent_id_fkey', 'represent', type_='foreignkey')
    op.drop_column('represent', 'represent_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('represent', sa.Column('represent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('represent_represent_id_fkey', 'represent', 'news', ['represent_id'], ['id'])
    op.drop_column('represent', 'id')
    op.add_column('interested', sa.Column('contact_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('interested_contact_id_fkey', 'interested', 'news', ['contact_id'], ['id'])
    op.drop_column('interested', 'id')
    op.add_column('fan', sa.Column('fan_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('fan_fan_id_fkey', 'fan', 'news', ['fan_id'], ['id'])
    op.drop_column('fan', 'id')
    op.add_column('established', sa.Column('established_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('established_established_id_fkey', 'established', 'news', ['established_id'], ['id'])
    op.drop_column('established', 'id')
    op.drop_table('specData')
    op.drop_table('keySpec')
    op.drop_table('gallery')
    # ### end Alembic commands ###
