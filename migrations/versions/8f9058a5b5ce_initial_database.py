"""Initial database

Revision ID: 8f9058a5b5ce
Revises: 
Create Date: 2020-10-27 17:19:35.179076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f9058a5b5ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info_soporte',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=255), nullable=True),
    sa.Column('marca', sa.String(length=255), nullable=True),
    sa.Column('modelo', sa.String(length=255), nullable=True),
    sa.Column('sn', sa.String(length=255), nullable=True),
    sa.Column('tinco', sa.String(length=255), nullable=True),
    sa.Column('plataforma', sa.String(length=255), nullable=True),
    sa.Column('datacenter', sa.String(length=255), nullable=True),
    sa.Column('sala', sa.String(length=255), nullable=True),
    sa.Column('rack', sa.String(length=255), nullable=True),
    sa.Column('proveedor', sa.String(length=255), nullable=True),
    sa.Column('soporte', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info_soporte')
    # ### end Alembic commands ###
