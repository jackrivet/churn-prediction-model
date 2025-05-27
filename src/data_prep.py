import pandas as pd
from src.connect_db import get_connection
def load_data(query_path: str):
    conn = get_connection()
    with open(query_path, 'r') as f:
        query = f.read()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
