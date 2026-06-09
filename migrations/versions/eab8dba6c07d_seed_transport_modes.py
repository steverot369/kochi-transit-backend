"""seed transport modes

Revision ID: eab8dba6c07d
Revises: f3aa3884e8ef
Create Date: 2026-06-09 21:17:25.847864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eab8dba6c07d'
down_revision: Union[str, Sequence[str], None] = 'f3aa3884e8ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.execute(
        """
        INSERT INTO transport_modes
        (name)

        VALUES

        ('Metro'),
        ('Water Metro'),
        ('Feeder Bus');
        """
    )


def downgrade():

    op.execute(
        """
        DELETE FROM transport_modes;
        """
    )