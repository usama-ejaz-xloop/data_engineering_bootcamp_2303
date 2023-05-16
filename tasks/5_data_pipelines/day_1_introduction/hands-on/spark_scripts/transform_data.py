import sys

from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.config(
    "Airflow Example - transform data"
).getOrCreate()


def transform_data(data_path: str) -> None:
    # TODO: write required operations. Save obtained DataFrames as
    #  "{data_path}/grouped_by_rating.csv"
    #  "{data_path}/mean_u1_rating.csv"
    #  "{data_path}/top_10.csv"
    pass


def main():
    data_path = sys.argv[1]
    transform_data(data_path)


if __name__ == "__main__":
    main()
