import fire
import mlflow
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def preprocess_data(df: pd.DataFrame):

    seasons = {1: "winter", 2: "spring", 3: "summer", 4: "fall"}

    # recoding seasons
    df["season"] = df["season"].map(seasons)

    # ## Cross-validation

    # Random split into train and test set is not a good idea here. Why?
    #
    # Instead, we take data from 2011 to the train set and from 2012 to the test set.
    return df


# we use scikit-learn pipeline to package standarization into single object with model
def setup_knn_pipeline(k):
    knn = KNeighborsClassifier(n_neighbors=k)
    pipe = make_pipeline(StandardScaler(), knn)
    return pipe


def split_data(df, train_max_date="2012-01-01"):
    train_mask = df.dteday < train_max_date
    df_train = df[train_mask]
    df_test = df[~train_mask]

    feature_1 = "temp"
    feature_2 = "casual"

    X_train = df_train[[feature_1, feature_2]]
    X_test = df_test[[feature_1, feature_2]]

    Y_train = df_train["season"] == "winter"
    Y_test = df_test["season"] == "winter"
    return X_train, X_test, Y_train, Y_test


def track_with_mlflow(model, X_test, Y_test, mlflow, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("accuracy", model.score(X_test, Y_test))
    mlflow.sklearn.log_model(model, "knn", registered_model_name="sklearn_knn")


def main(file_name: str, max_k: int):
    df = preprocess_data(pd.read_csv(file_name))

    X_train, X_test, Y_train, Y_test = split_data(df)
    # let's check some other k
    k_list = range(1, max_k)

    for k in k_list:
        with mlflow.start_run():
            knn_pipe = setup_knn_pipeline(k)
            knn_pipe.fit(X_train, Y_train)
            model_metadata = {"k": k}
            track_with_mlflow(knn_pipe, X_test, Y_test, mlflow, model_metadata)


if __name__ == "__main__":
    fire.Fire(main)
