from TextSummarizer.config.configuration import ConfigManager 
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform_data()