import pandas as pd
import utils
import cleaning
import fire
from typing import List


def filter_input_data(
    data_path: str,
    target_col: str,
    dropped_values: List[str],
    replace_by_zero: str,
    max_nan_proportion: float,
    max_categorical_cardinality: int,
    dst_filename: str,
    selected_cols: List[str],
):
    csv_path = data_path
    df = pd.read_csv(csv_path)
    # we take every 100th record for performance reasons
    df = df.iloc[::100, :].reset_index(drop=True)
    cleaned_df = cleaning.filter_df(
        df,
        target_col,
        dropped_values,
        replace_by_zero,
        max_nan_proportion,
        max_categorical_cardinality,
    )
    selected_cols = list(cleaned_df.select_dtypes("object").columns) + ["target"]
    cleaned_df[selected_cols].reset_index().to_parquet(str(dst_filename), index=False)


def prepare_train_test_split(
    data_path: str,
    last_train_issue_date: str,
    last_test_issue_date: str,
    train_path: str,
    test_path: str,
):
    df = utils.read_parquet(data_path)
    last_train_issue_date = pd.to_datetime(last_train_issue_date)
    last_test_issue_date = pd.to_datetime(last_test_issue_date)
    date_col = pd.to_datetime(df["issue_d"])
    train_df = df[date_col <= last_train_issue_date]
    test_df = df[
        (last_train_issue_date < date_col) & (date_col <= last_test_issue_date)
    ]
    train_df.to_parquet(train_path, index=False)
    test_df.to_parquet(test_path, index=False)


if __name__ == "__main__":
    fire.Fire()
