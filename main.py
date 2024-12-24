from src.cnnClassifier.loggs import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> satge {STAGE_NAME} started ")
    obj= DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>> satge {STAGE_NAME} completed ")
    
except Exception as e:
    logger.exception(e)
    raise e