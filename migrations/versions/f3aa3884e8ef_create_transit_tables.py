"""create transit tables

Revision ID: f3aa3884e8ef
Revises: 17266f9c10b6
Create Date: 2026-06-09 21:16:50.181378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3aa3884e8ef'
down_revision: Union[str, Sequence[str], None] = '17266f9c10b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def base_columns():

    return [

        sa.Column(
            "id",
            sa.BigInteger(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "uuid",
            sa.UUID(),
            nullable=False,
            unique=True,
            server_default=sa.text(
                "gen_random_uuid()"
            )
        ),

        sa.Column(
            "status",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text(
                "true"
            )
        ),

        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            )
        ),

        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            )
        ),

        sa.Column(
            "created_by",
            sa.UUID(),
            nullable=True
        ),

        sa.Column(
            "updated_by",
            sa.UUID(),
            nullable=True
        ),

        sa.Column(
            "deleted_at",
            sa.TIMESTAMP(),
            nullable=True
        )

    ]


def upgrade():

    # -----------------------
    # TRANSPORT MODES
    # -----------------------

    op.create_table(

        "transport_modes",

        *base_columns(),

        sa.Column(
            "name",
            sa.String(100),
            nullable=False,
            unique=True
        )

    )

    # -----------------------
    # STOPS
    # -----------------------

    op.create_table(

        "stops",

        *base_columns(),

        sa.Column(
            "stop_code",
            sa.String(50),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "stop_name",
            sa.String(200),
            nullable=False
        ),

        sa.Column(
            "search_name",
            sa.String(300)
        ),

        sa.Column(
            "transport_mode_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "transport_modes.id"
            )
        ),

        sa.Column(
            "latitude",
            sa.Numeric(10, 7)
        ),

        sa.Column(
            "longitude",
            sa.Numeric(10, 7)
        ),

        sa.Column(
            "is_interchange",
            sa.Boolean(),
            server_default=sa.text(
                "false"
            )
        )

    )

    # -----------------------
    # ROUTES
    # -----------------------

    op.create_table(

        "routes",

        *base_columns(),

        sa.Column(
            "route_code",
            sa.String(50),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "route_name",
            sa.String(300)
        ),

        sa.Column(
            "transport_mode_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "transport_modes.id"
            )
        )

    )

    # -----------------------
    # TRIPS
    # -----------------------

    op.create_table(

        "trips",

        *base_columns(),

        sa.Column(
            "trip_code",
            sa.String(100),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "route_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "routes.id"
            )
        ),

        sa.Column(
            "service_type",
            sa.String(100)
        )

    )

    # -----------------------
    # TRIP STOP TIMES
    # -----------------------

    op.create_table(

        "trip_stop_times",

        *base_columns(),

        sa.Column(
            "trip_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "trips.id"
            )
        ),

        sa.Column(
            "stop_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "stops.id"
            )
        ),

        sa.Column(
            "stop_sequence",
            sa.Integer()
        ),

        sa.Column(
            "arrival_time",
            sa.Time()
        ),

        sa.Column(
            "departure_time",
            sa.Time()
        )

    )

    # -----------------------
    # INTERCHANGE
    # -----------------------

    op.create_table(

        "interchange_points",

        *base_columns(),

        sa.Column(
            "from_stop_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "stops.id"
            )
        ),

        sa.Column(
            "to_stop_id",
            sa.BigInteger(),
            sa.ForeignKey(
                "stops.id"
            )
        ),

        sa.Column(
            "transfer_type",
            sa.String(100)
        ),

        sa.Column(
            "walking_distance",
            sa.Integer()
        ),

        sa.Column(
            "walking_minutes",
            sa.Integer()
        ),

        sa.Column(
            "remarks",
            sa.Text()
        )

    )

    # -----------------------
    # INDEXES
    # -----------------------

    op.create_index(
        "idx_stop_code",
        "stops",
        ["stop_code"]
    )

    op.create_index(
        "idx_trip_code",
        "trips",
        ["trip_code"]
    )

    op.create_index(
        "idx_route_code",
        "routes",
        ["route_code"]
    )


def downgrade():

    op.drop_index(
        "idx_route_code",
        table_name="routes"
    )

    op.drop_index(
        "idx_trip_code",
        table_name="trips"
    )

    op.drop_index(
        "idx_stop_code",
        table_name="stops"
    )

    op.drop_table(
        "interchange_points"
    )

    op.drop_table(
        "trip_stop_times"
    )

    op.drop_table(
        "trips"
    )

    op.drop_table(
        "routes"
    )

    op.drop_table(
        "stops"
    )

    op.drop_table(
        "transport_modes"
    )
