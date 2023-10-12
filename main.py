from TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from TextSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline
from TextSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from TextSummarizer.logging import logger



try :
    STAGE_NAME = 'Data Ingestion Stage'
    logger.info(f"<<<{STAGE_NAME} Started>>>")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.run()
    logger.info(f"<<<{STAGE_NAME} Ended>>>")
    
except Exception as e:
    logger.exception(STAGE_NAME, e)
    raise  e 

try :
    STAGE_NAME = 'Data Validation Stage'
    logger.info(f"<<<{STAGE_NAME} Started>>>")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.run()
    logger.info(f"<<<{STAGE_NAME} Ended>>>")
except Exception as e:
    logger.exception(STAGE_NAME, e)
    raise  e 

try :
    STAGE_NAME = 'Data Transformation Stage'
    logger.info(f"<<<{STAGE_NAME} Started>>>")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.run()
    logger.info(f"<<<{STAGE_NAME} Ended>>>")
except Exception as e:
    logger.exception(STAGE_NAME, e)
    raise  e 