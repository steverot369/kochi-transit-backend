"""add time seconds columns

Revision ID: 957f811861ac
Revises: c018113f36d4
Create Date: 2026-06-09 22:01:49.201830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '957f811861ac'
down_revision: Union[str, Sequence[str], None] = 'c018113f36d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.add_column(
        "trip_stop_times",
        sa.Column(
            "arrival_seconds",
            sa.Integer(),
            nullable=True
        )
    )

    op.add_column(
        "trip_stop_times",
        sa.Column(
            "departure_seconds",
            sa.Integer(),
            nullable=True
        )
    )


def downgrade():

    op.drop_column(
        "trip_stop_times",
        "departure_seconds"
    )

    op.drop_column(
        "trip_stop_times",
        "arrival_seconds"
    )