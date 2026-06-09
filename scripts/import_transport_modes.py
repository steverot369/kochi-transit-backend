import pandas as pd
from sqlalchemy import text

from db import SessionLocal

CSV_FILE = "../data/transport_modes.csv"

db = SessionLocal()

df = pd.read_csv(CSV_FILE)

for _, row in df.iterrows():

    check = db.execute(
        text("""
        SELECT id
        FROM transport_modes
        WHERE name=:name
        """),
        {
            "name": row["mode_name"]
        }
    ).fetchone()

    if check:
        continue

    db.execute(
        text("""
        INSERT INTO transport_modes
        (name)

        VALUES

        (:name)
        """),
        {
            "name": row["mode_name"]
        }
    )

db.commit()

db.close()

print("Transport Modes Imported")