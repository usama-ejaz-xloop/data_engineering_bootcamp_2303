from typing import List
import pandas as pd


def filter_target_col(
    df, target_col: str, dropped_values: List[str], replace_by_zero: str
):
    """
    filtering dataframe:
    - preparing target column
    - removing examples with `target_col` in `dropped_values`
    """
    cleaned_df = df[~df[target_col].str.lower().isin(dropped_values)]
    target = cleaned_df[target_col].str.lower() != replace_by_zero
    target = target.fillna(1)
    cleaned_df["target"] = target
    return cleaned_df


def get_too_big_categorical_columns(df, max_categorical_cardinality):
    categorical_columns = list(df.select_dtypes("object").columns)
    categorical_counts = pd.Series(
        {col: len(df[col].unique()) for col in categorical_columns}
    ).sort_values(ascending=False)
    return list(
        categorical_counts[categorical_counts > max_categorical_cardinality].index
    )


def get_invalid_nan_cols(df, max_nan_proportion):
    na_cols = [col for col in df.columns if df[col].isna().mean() > max_nan_proportion]
    return na_cols


def filter_invalid_columns(df, max_nan_proportion, max_categorical_cardinality):
    na_cols = get_invalid_nan_cols(df, max_nan_proportion)
    too_big_categorical_cols = get_too_big_categorical_columns(
        df, max_categorical_cardinality
    )
    return df.drop(columns=na_cols + too_big_categorical_cols)


def filter_df(
    df,
    target_col: str,
    dropped_values: List[str],
    replace_by_zero: str,
    max_nan_proportion: float,
    max_categorical_cardinality: int,
):
    filtered_rows_df = filter_target_col(
        df, target_col, dropped_values, replace_by_zero
    )
    filtered_df = filter_invalid_columns(
        filtered_rows_df, max_nan_proportion, max_categorical_cardinality
    )
    return filtered_df.drop(columns=[target_col])
