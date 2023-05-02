import pandas as pd
import os


def prepare_input(data_dir, filename):

    train_df = read_parquet(os.path.join(data_dir, filename + ".parquet"))

    X_train = train_df.drop(columns=["target"])
    y_train = train_df["target"]
    return X_train, y_train


def read_parquet(path):
    df = pd.read_parquet(path)
    if "index" in df.columns:
        return df.drop(columns=["index"])
    else:
        return df
