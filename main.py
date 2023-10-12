from TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from TextSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion Stage'

try :
    logger.info(f"<<<{STAGE_NAME} Started>>>")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"<<<{STAGE_NAME} Ended>>>")
    
except Exception as e:
    logger.exception(STAGE_NAME, e)
    raise  e 
