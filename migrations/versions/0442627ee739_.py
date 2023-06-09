"""empty message

Revision ID: 0442627ee739
Revises: 2572225a83ae
Create Date: 2023-04-25 16:50:50.573744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0442627ee739'
down_revision = '2572225a83ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fav__people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fav__planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=50), nullable=True),
    sa.Column('skin_color', sa.String(length=50), nullable=True),
    sa.Column('eye_color', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=True),
    sa.Column('rotation_period', sa.String(length=50), nullable=True),
    sa.Column('orbital_period', sa.String(length=50), nullable=True),
    sa.Column('diameter', sa.String(length=50), nullable=True),
    sa.Column('gravity', sa.String(length=50), nullable=True),
    sa.Column('population', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('fav__planets')
    op.drop_table('fav__people')
    # ### end Alembic commands ###
