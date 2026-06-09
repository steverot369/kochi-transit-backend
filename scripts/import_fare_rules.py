import pandas as pd
import uuid

from sqlalchemy import text

from db import SessionLocal

CSV_FILE = "../data/fare_rules.csv"

db = SessionLocal()

df = pd.read_csv(CSV_FILE)

for _, row in df.iterrows():

    # -----------------------------------
    # Find Fare Attribute
    # -----------------------------------

    fare = db.execute(

        text("""

        SELECT id

        FROM fare_attributes

        WHERE fare_id=:fare_id

        """),

        {

            "fare_id":
            row["fare_id"]

        }

    ).fetchone()

    if not fare:

        print(
            f"Fare not found : {row['fare_id']}"
        )

        continue

    fare_attribute_id = fare[0]

    route_id = None
    origin_stop_id = None
    destination_stop_id = None

    # -----------------------------------
    # Route Based Fare
    # -----------------------------------

    if pd.notna(row["route_id"]):

        route = db.execute(

            text("""

            SELECT id

            FROM routes

            WHERE route_code=:code

            """),

            {

                "code":
                row["route_id"]

            }

        ).fetchone()

        if route:

            route_id = route[0]

    # -----------------------------------
    # Origin Stop
    # -----------------------------------

    if pd.notna(row["origin_id"]):

        origin = db.execute(

            text("""

            SELECT id

            FROM stops

            WHERE stop_code=:code

            """),

            {

                "code":
                row["origin_id"]

            }

        ).fetchone()

        if origin:

            origin_stop_id = origin[0]

    # -----------------------------------
    # Destination Stop
    # -----------------------------------

    if pd.notna(row["destination_id"]):

        destination = db.execute(

            text("""

            SELECT id

            FROM stops

            WHERE stop_code=:code

            """),

            {

                "code":
                row["destination_id"]

            }

        ).fetchone()

        if destination:

            destination_stop_id = destination[0]

    # -----------------------------------
    # Insert
    # -----------------------------------

    db.execute(

        text("""

        INSERT INTO fare_rules

        (

            uuid,

            fare_attribute_id,

            route_id,

            origin_stop_id,

            destination_stop_id

        )

        VALUES

        (

            :uuid,

            :fare_attribute_id,

            :route_id,

            :origin_stop_id,

            :destination_stop_id

        )

        """),

        {

            "uuid":
            str(
                uuid.uuid4()
            ),

            "fare_attribute_id":
            fare_attribute_id,

            "route_id":
            route_id,

            "origin_stop_id":
            origin_stop_id,

            "destination_stop_id":
            destination_stop_id

        }

    )

db.commit()

db.close()

print("Fare Rules Imported Successfully")