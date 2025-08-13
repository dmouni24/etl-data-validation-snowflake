import os
from dotenv import load_dotenv
import pandas as pd
import snowflake.connector

load_dotenv()

def get_conn():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

def row_count(cur, table):
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    return cur.fetchone()[0]

def validate_counts(staging, target):
    with get_conn() as conn:
        cur = conn.cursor()
        s = row_count(cur, staging)
        t = row_count(cur, target)
        assert s == t, f"Row count mismatch: {staging}={s}, {target}={t}"

if __name__ == "__main__":
    # Example usage
    validate_counts("STG.CUSTOMERS", "DW.CUSTOMERS")
