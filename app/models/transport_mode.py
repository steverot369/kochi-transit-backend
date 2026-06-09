from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import String

from app.core.database import Base


class TransportMode(Base):

    __tablename__ = "transport_modes"

    id = Column(
        BigInteger,
        primary_key=True
    )

    uuid = Column(String)

    name = Column(String)