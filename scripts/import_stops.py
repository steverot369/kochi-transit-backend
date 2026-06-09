import pandas as pd
from sqlalchemy import text

from db import SessionLocal

db = SessionLocal()

df = pd.read_csv("../data/stops.csv")

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

        INSERT INTO stops

        (
            stop_code,
            stop_name,
            transport_mode_id,
            latitude,
            longitude
        )

        VALUES

        (
            :stop_code,
            :stop_name,
            :transport_mode_id,
            :latitude,
            :longitude
        )

        ON CONFLICT(stop_code)

        DO NOTHING

        """),

        {

            "stop_code": row["stop_code"],
            "stop_name": row["stop_name"],
            "transport_mode_id": mode[0],
            "latitude": row["latitude"],
            "longitude": row["longitude"]

        }

    )

db.commit()
db.close()

print("Stops Imported")