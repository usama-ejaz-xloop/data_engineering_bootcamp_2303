import sys
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.config("Airflow Example - join data").getOrCreate()


def join_data(data_path: str) -> None:
    # TODO: write required operations. Save obtained DataFrame as "{data_path}/joined_df.csv"
    pass


def main():
    data_path = sys.argv[1]
    join_data(data_path)


if __name__ == "__main__":
    main()
