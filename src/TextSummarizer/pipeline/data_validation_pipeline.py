from TextSummarizer.config.configuration import ConfigManager 
from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()

