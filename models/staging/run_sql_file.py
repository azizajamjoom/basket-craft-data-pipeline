import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Pull values from .env
pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_host = os.getenv("PG_HOST")
pg_db = os.getenv("PG_DB")

# Create connection
pg_engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}")

# Load SQL from file
with open("models/staging/stg_website_sessions.sql", "r") as f:
    query = f.read()

# Execute query
df = pd.read_sql(query, pg_engine)

# Preview result
print(df.head())