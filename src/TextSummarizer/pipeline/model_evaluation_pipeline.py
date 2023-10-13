from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.components.model_evaluation import ModelEvaluation
from TextSummarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()