from TextSummarizer.config.configuration import ConfigManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()