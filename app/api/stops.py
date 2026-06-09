from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from sqlalchemy import text

from app.core.database import get_db

router = APIRouter()


@router.get("/stops")
def get_stops(
    db: Session = Depends(get_db)
):

    rows = db.execute(

        text("""

        SELECT

            s.id,

            s.uuid,

            s.stop_code,

            s.stop_name,

            s.latitude,

            s.longitude,

            tm.name
            AS transport_mode

        FROM stops s

        JOIN transport_modes tm

        ON s.transport_mode_id=tm.id

        ORDER BY

        s.stop_name

        """)

    ).fetchall()

    result = []

    for row in rows:

        result.append(

            {

                "id":
                row.id,

                "uuid":
                str(
                    row.uuid
                ),

                "stop_code":
                row.stop_code,

                "stop_name":
                row.stop_name,

                "latitude":
                float(
                    row.latitude
                )
                if row.latitude
                else None,

                "longitude":
                float(
                    row.longitude
                )
                if row.longitude
                else None,

                "transport_mode":
                row.transport_mode

            }

        )

    return result