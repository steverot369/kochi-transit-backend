"""change trip stop times to string

Revision ID: c018113f36d4
Revises: eab8dba6c07d
Create Date: 2026-06-09 22:01:02.018146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c018113f36d4'
down_revision: Union[str, Sequence[str], None] = 'eab8dba6c07d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.alter_column(
        "trip_stop_times",
        "arrival_time",
        existing_type=sa.Time(),
        type_=sa.String(length=8),
        existing_nullable=True,
        postgresql_using="arrival_time::text"
    )

    op.alter_column(
        "trip_stop_times",
        "departure_time",
        existing_type=sa.Time(),
        type_=sa.String(length=8),
        existing_nullable=True,
        postgresql_using="departure_time::text"
    )


def downgrade():

    op.alter_column(
        "trip_stop_times",
        "departure_time",
        existing_type=sa.String(length=8),
        type_=sa.Time(),
        existing_nullable=True,
        postgresql_using="departure_time::time"
    )

    op.alter_column(
        "trip_stop_times",
        "arrival_time",
        existing_type=sa.String(length=8),
        type_=sa.Time(),
        existing_nullable=True,
        postgresql_using="arrival_time::time"
    )
