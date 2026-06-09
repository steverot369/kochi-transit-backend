import pandas as pd
from sqlalchemy import text

from db import SessionLocal

db = SessionLocal()

df = pd.read_csv("../data/routes.csv")

for _, row in df.iterrows():

    mode = db.execute(

        text("""

        SELECT id

        FROM transport_modes

        WHERE name=:name

        """),

        {
            "name": row["transport_mode"]
        }

    ).fetchone()

    if not mode:
        continue

    db.execute(

        text("""

        INSERT INTO routes

        (
            route_code,
            route_name,
            transport_mode_id
        )

        VALUES

        (
            :route_code,
            :route_name,
            :transport_mode_id
        )

        ON CONFLICT(route_code)

        DO NOTHING

        """),

        {

            "route_code": row["route_code"],
            "route_name": row["route_name"],
            "transport_mode_id": mode[0]

        }

    )

db.commit()
db.close()

print("Routes Imported")