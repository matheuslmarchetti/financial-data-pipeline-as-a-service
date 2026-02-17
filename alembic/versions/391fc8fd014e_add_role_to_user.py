"""add role to user

Revision ID: 391fc8fd014e
Revises: 5c499684935a
Create Date: 2026-02-17 13:51:04.761170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '391fc8fd014e'
down_revision: Union[str, Sequence[str], None] = '5c499684935a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Criar o tipo ENUM manualmente
    userrole = sa.Enum('admin', 'user', name='userrole')
    userrole.create(op.get_bind())

    # Adicionar coluna com default temporário
    op.add_column(
        'users',
        sa.Column(
            'role',
            userrole,
            nullable=False,
            server_default='user'
        )
    )

    # Remover default depois de popular
    op.alter_column('users', 'role', server_default=None)


def downgrade():
    op.drop_column('users', 'role')
    sa.Enum(name='userrole').drop(op.get_bind())
