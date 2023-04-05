import mlflow
import pandas as pd
from sklearn import metrics
import fire


def get_auc_score(model, df):
    X_df = df.drop(columns=["target"])
    y = df["target"]
    y_pred = model.predict(X_df)
    return metrics.roc_auc_score(y, y_pred)


def main(model_path, model_version, data_path, data_version):
    df = pd.read_parquet(data_path.format(data_version))
    model = mlflow.pyfunc.load_model(model_path.format(model_version))
    auc = get_auc_score(model, df)
    print(
        "Test data version {}, model version {}, AUC: {}".format(
            data_version, model_version, auc
        )
    )

    with mlflow.start_run():
        mlflow.log_metric("AUC", auc)


if __name__ == "__main__":
    fire.Fire(main)
