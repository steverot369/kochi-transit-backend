"""initial transit schema

Revision ID: e96a92b93ee2
Revises: 
Create Date: 2026-06-09 21:13:13.721145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e96a92b93ee2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        """
        CREATE EXTENSION IF NOT EXISTS pgcrypto;
        """
    )


def downgrade():
    op.execute(
        """
        DROP EXTENSION IF EXISTS pgcrypto;
        """
    )
