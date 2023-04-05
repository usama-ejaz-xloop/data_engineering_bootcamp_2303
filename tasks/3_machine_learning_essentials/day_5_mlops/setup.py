from lending_club.models import pipelines, configs
import pickle


def setup_simple_pipeline(config_dict):
    config = configs.PipelineConfig(**config_dict)
    return pipelines.get_classification_pipeline(config)


def make_simple_pipeline(config_dict, product):
    pipeline = setup_simple_pipeline(config_dict)
    with open(str(product), "wb") as f:
        pickle.dump(pipeline, f)
