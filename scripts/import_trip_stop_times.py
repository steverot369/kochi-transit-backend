import pandas as pd
from sqlalchemy import text

from db import SessionLocal

db = SessionLocal()

df = pd.read_csv("../data/trip_stop_times.csv")

for _, row in df.iterrows():

    trip = db.execute(

        text("""

        SELECT id

        FROM trips

        WHERE trip_code=:trip

        """),

        {
            "trip": row["trip_code"]
        }

    ).fetchone()

    if not trip:
        continue

    stop = db.execute(

        text("""

        SELECT id

        FROM stops

        WHERE stop_name=:stop

        """),

        {
            "stop": row["stop_name"]
        }

    ).fetchone()

    if not stop:
        continue

    db.execute(

        text("""

        INSERT INTO trip_stop_times

        (
            trip_id,
            stop_id,
            stop_sequence,
            arrival_time,
            departure_time
        )

        VALUES

        (
            :trip_id,
            :stop_id,
            :stop_sequence,
            :arrival_time,
            :departure_time
        )

        """),

        {

            "trip_id": trip[0],
            "stop_id": stop[0],
            "stop_sequence": int(row["stop_sequence"]),
            "arrival_time": row["arrival_time"],
            "departure_time": row["departure_time"]

        }

    )

db.commit()
db.close()

print("Trip Stop Times Imported")