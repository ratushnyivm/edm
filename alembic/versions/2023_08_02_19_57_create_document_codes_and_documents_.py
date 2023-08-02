"""create document_codes and documents tables

Revision ID: 160659b7bc76
Revises:
Create Date: 2023-08-02 19:57:45.530396

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '160659b7bc76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'document_codes',

        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('code', sa.String(length=5), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('code')
    )
    op.create_table(
        'documents',

        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('number', sa.String(length=30), nullable=False),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('document_code_id', sa.Integer(), nullable=False),
        sa.Column('document_code_number', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(['document_code_id'], ['document_codes.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('documents')
    op.drop_table('document_codes')
    # ### end Alembic commands ###