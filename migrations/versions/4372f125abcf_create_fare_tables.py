"""create fare tables

Revision ID: 4372f125abcf
Revises: 957f811861ac
Create Date: 2026-06-09 23:39:38.343063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4372f125abcf'
down_revision: Union[str, Sequence[str], None] = '957f811861ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    # ==================================================
    # FARE ATTRIBUTES
    # ==================================================

    op.create_table(

        "fare_attributes",

        sa.Column(
            "id",
            sa.BigInteger(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "uuid",
            sa.String(36),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "fare_id",
            sa.String(50),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "price",
            sa.Numeric(10, 2),
            nullable=False
        ),

        sa.Column(
            "currency_type",
            sa.String(10),
            nullable=False
        ),

        sa.Column(
            "payment_method",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "transfers",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "transfer_duration",
            sa.Integer(),
            nullable=False
        )

    )

    # ==================================================
    # FARE RULES
    # ==================================================

    op.create_table(

        "fare_rules",

        sa.Column(
            "id",
            sa.BigInteger(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "uuid",
            sa.String(36),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "fare_attribute_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "fare_attributes.id"
            ),
            nullable=False
        ),

        sa.Column(
            "route_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "routes.id"
            ),
            nullable=True
        ),

        sa.Column(
            "origin_stop_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "stops.id"
            ),
            nullable=False
        ),

        sa.Column(
            "destination_stop_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "stops.id"
            ),
            nullable=False
        )

    )

    # Unique fare between two stops

    op.create_unique_constraint(

        "uq_fare_rule",

        "fare_rules",

        [

            "origin_stop_id",

            "destination_stop_id"

        ]

    )


def downgrade():

    op.drop_constraint(
        "uq_fare_rule",
        "fare_rules",
        type_="unique"
    )

    op.drop_table(
        "fare_rules"
    )

    op.drop_table(
        "fare_attributes"
    )