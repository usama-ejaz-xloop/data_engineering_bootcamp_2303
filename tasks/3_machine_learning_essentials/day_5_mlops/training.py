# %%
import logging

import fire
import mlflow
import yaml
from sklearn import metrics

import configs
import pipelines
import utils
from sklearn import metrics

logging.basicConfig(level="INFO")


def train_model(data_dir: str, config_dict_path: str, data_version: str):
    with open(config_dict_path, "r") as f:
        config_dict = yaml.safe_load(f)
    config = configs.PipelineConfig(**config_dict)

    with mlflow.start_run():
        mlflow.log_params(config_dict)
        clf_pipeline = pipelines.get_classification_pipeline(config)
        X_train, y_train = utils.prepare_input(data_dir, "train" + data_version)

        clf_pipeline.fit(X_train, y_train)
        f1_score = metrics.f1_score(y_train, clf_pipeline.predict(X_train))

        mlflow.log_metric("training_f1", f1_score)
        mlflow.sklearn.log_model(
            clf_pipeline,
            "model",
            registered_model_name="ChurnModel" + "_" + data_version,
            signature=mlflow.models.infer_signature(X_train),
        )


if __name__ == "__main__":
    fire.Fire()
