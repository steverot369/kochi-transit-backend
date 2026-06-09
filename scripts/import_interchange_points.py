import pandas as pd
from sqlalchemy import text

from db import SessionLocal

db = SessionLocal()

df = pd.read_csv(
    "../data/interchange_points.csv"
)

for _, row in df.iterrows():

    from_stop = db.execute(

        text("""

        SELECT id

        FROM stops

        WHERE stop_code=:code

        """),

        {
            "code":
            row["from_stop_code"]
        }

    ).fetchone()

    to_stop = db.execute(

        text("""

        SELECT id

        FROM stops

        WHERE stop_code=:code

        """),

        {
            "code":
            row["to_stop_code"]
        }

    ).fetchone()

    if not from_stop or not to_stop:
        continue

    db.execute(

        text("""

        INSERT INTO
        interchange_points

        (

            from_stop_id,

            to_stop_id,

            transfer_type,

            walking_distance,

            walking_minutes,

            remarks

        )

        VALUES

        (

            :from_stop_id,

            :to_stop_id,

            :transfer_type,

            :walking_distance,

            :walking_minutes,

            :remarks

        )

        """),

        {

            "from_stop_id":
                from_stop[0],

            "to_stop_id":
                to_stop[0],

            "transfer_type":
                row["transfer_type"],

            "walking_distance":
                row["walking_distance"],

            "walking_minutes":
                row["walking_minutes"],

            "remarks":
                row["remarks"]

        }

    )

db.commit()
db.close()

print("Interchange Imported")