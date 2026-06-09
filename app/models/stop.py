from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from app.core.database import Base


class Stop(Base):

    __tablename__ = "stops"

    id = Column(
        BigInteger,
        primary_key=True
    )

    uuid = Column(String)

    stop_code = Column(String)

    stop_name = Column(String)

    search_name = Column(String)

    transport_mode_id = Column(
        BigInteger,
        ForeignKey(
            "transport_modes.id"
        )
    )

    latitude = Column(
        Numeric
    )

    longitude = Column(
        Numeric
    )

    is_interchange = Column(
        Boolean
    )