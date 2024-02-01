import pandas as pd
import pyarrow
from sqlalchemy import create_engine
import argparse
import os


def main(params):
    port  = params.port
    engine = create_engine(f'postgresql://{params.user}:{params.password}@{params.host}:{port}/{params.db}')
    
    file_name = 'output.parquet'

    os.system(f"wget {params.url} -O {file_name}")

    df = pd.read_parquet(file_name)

    df.head(0).to_sql(name=params.table_name, con=engine, if_exists='replace')

    print("Started data ingestion")
    df.to_sql(name=params.table_name, con=engine, if_exists='append')
    print("Data ingestion completed")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres')

    parser.add_argument('--user', help='User name for postgres')
    parser.add_argument('--password', help='Password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--url', help='url of the parquet file')
    parser.add_argument('--table_name', help='name of the table to write result in postgres')

    args = parser.parse_args()

    main(args)


