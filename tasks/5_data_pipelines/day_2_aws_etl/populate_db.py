import pandas as pd
from psycopg2 import OperationalError
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


class DatabaseConnector:
    def __init__(self, drivername, database, username, host, password):
        self.drivername = drivername
        self.database = database
        self.username = username
        self.host = host
        self.password = password

        self.engine = create_engine(
            URL.create(
                drivername=self.drivername,
                database=self.database,
                username=self.username,
                host=self.host,
                password=self.password,
                port=5432,
            )
        )

    def get_engine(self):
        return self.engine

    def populate_db_with_df_data(
        self, table_name: str, primary_key: str, df: pd.DataFrame
    ):
        df.to_sql(
            name=table_name,
            con=self.engine,
            if_exists="replace",
            index=False,
        )
        self.run_raw_query(
            f"""ALTER TABLE {table_name} ADD CONSTRAINT employee_id_pk PRIMARY KEY ("{primary_key}");"""
        )

    def run_raw_query(self, query):
        with self.engine.connect() as con:
            statement = text(query)
            return con.execute(statement)


def main():
    try:
        db_connector = DatabaseConnector(
            drivername="postgresql",
            database="employees_db",
            # username you set during the creation of the database
            username="<your_username>",
            # endpoint url, to be found in the `Connectivity & security` section in RDS
            host="<your_connection_endpoint_url>",
            # password you set during the creation of the database
            password="<password>",
        )
    except OperationalError:
        raise ConnectionError("Could not establish DB connection.")

    employee_df = pd.read_csv("data/employees.csv")

    table_name = "employees"
    primary_key = "emp_id"

    # populate the database
    db_connector.populate_db_with_df_data(
        table_name=table_name, primary_key=primary_key, df=employee_df
    )

    # check if the data is in place
    result = db_connector.run_raw_query(f"""SELECT * FROM "{table_name}" limit 10;""")

    for row in result:
        print(row)


if __name__ == "__main__":
    main()
