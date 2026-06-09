import pandas as pd
import uuid

from sqlalchemy import text
from db import SessionLocal

CSV_FILE = "../data/fare_attributes.csv"

db = SessionLocal()

df = pd.read_csv(CSV_FILE)

for _, row in df.iterrows():

    db.execute(

        text("""

        INSERT INTO fare_attributes

        (

            uuid,

            fare_id,

            price,

            currency_type,

            payment_method,

            transfers,

            transfer_duration

        )

        VALUES

        (

            :uuid,

            :fare_id,

            :price,

            :currency_type,

            :payment_method,

            :transfers,

            :transfer_duration

        )

        ON CONFLICT (fare_id)

        DO NOTHING

        """),

        {

            "uuid":
            str(
                uuid.uuid4()
            ),

            "fare_id":
            row["fare_id"],

            "price":
            float(
                row["price"]
            ),

            "currency_type":
            row["currency_type"],

            "payment_method":
            int(
                row["payment_method"]
            ),

            "transfers":
            int(
                row["transfers"]
            ),

            "transfer_duration":
            int(
                row["transfer_duration"]
            )

        }

    )

db.commit()

db.close()

print("Fare Attributes Imported Successfully")