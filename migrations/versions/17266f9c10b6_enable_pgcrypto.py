"""enable pgcrypto

Revision ID: 17266f9c10b6
Revises: e96a92b93ee2
Create Date: 2026-06-09 21:15:20.386833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17266f9c10b6'
down_revision: Union[str, Sequence[str], None] = 'e96a92b93ee2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
