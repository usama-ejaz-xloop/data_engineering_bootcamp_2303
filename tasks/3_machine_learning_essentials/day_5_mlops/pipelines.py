from sklearn import (
    compose,
    impute,
    pipeline,
)
import configs


def get_simple_input_encoding_pipeline(
    categorical_encoder_type: str, imputation_strategy: str
):
    return compose.ColumnTransformer(
        transformers=[
            (
                "numerical",
                impute.SimpleImputer(strategy=imputation_strategy),
                compose.make_column_selector(dtype_include="float"),
            ),
            (
                "categorical",
                compose.make_column_selector(dtype_exclude="float"),
            ),
        ]
    )


def get_classification_pipeline(config: configs.PipelineConfig):
    model = config.get_model()
    featurizer = configs._CATEGORICAL_ENCODER_MAPPING[config.categorical_encoder_type]
    maybe_feature_selector = config.get_feature_selector(model)
    if maybe_feature_selector is not None:
        steps = [featurizer, maybe_feature_selector, model]
    else:
        steps = [featurizer, model]
    return pipeline.make_pipeline(*steps)
