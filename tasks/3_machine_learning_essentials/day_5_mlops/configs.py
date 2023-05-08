from dataclasses import dataclass, field
from typing import Optional

from category_encoders import target_encoder
from sklearn import (
    ensemble,
    feature_selection,
    linear_model,
    preprocessing,
)

_MODEL_MAPPING = {
    "random_forest": ensemble.RandomForestClassifier,
    "logistic_regression": linear_model.LogisticRegression,
}

_CATEGORICAL_ENCODER_MAPPING = {
    "target_encoder": target_encoder.TargetEncoder(),
    "one_hot_encoder": preprocessing.OneHotEncoder(),
}

_FEATURE_SELECTOR_MAPPING = {
    "forward_stagewise": feature_selection.SequentialFeatureSelector
}


@dataclass
class PipelineConfig:
    model_type: str
    categorical_encoder_type: str
    model_config: dict = field(default_factory=dict)
    feature_selector: Optional[str] = field(default=None)
    feature_selector_config: Optional[dict] = field(default_factory=dict)
    imputation_strategy: str = field(default="median")

    def get_model(self):
        assert (
            self.model_type in _MODEL_MAPPING.keys()
        ), f"no such model {self.model_type}"
        return _MODEL_MAPPING[self.model_type](**self.model_config)

    def get_feature_selector(self, model):
        if self.feature_selector is not None:
            return _FEATURE_SELECTOR_MAPPING[self.feature_selector](
                model, **self.feature_selector_config
            )
