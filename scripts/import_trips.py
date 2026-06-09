import pandas as pd
from sqlalchemy import text

from db import SessionLocal

db = SessionLocal()

df = pd.read_csv("../data/trips.csv")

for _, row in df.iterrows():

    route = db.execute(

        text("""

        SELECT id

        FROM routes

        WHERE route_code=:code

        """),

        {
            "code": row["route_code"]
        }

    ).fetchone()

    if not route:
        continue

    db.execute(

        text("""

        INSERT INTO trips

        (
            trip_code,
            route_id
        )

        VALUES

        (
            :trip_code,
            :route_id
        )

        ON CONFLICT(trip_code)

        DO NOTHING

        """),

        {

            "trip_code": row["trip_code"],
            "route_id": route[0]

        }

    )

db.commit()
db.close()

print("Trips Imported")