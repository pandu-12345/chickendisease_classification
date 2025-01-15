from src.cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cnnClassifier.loggs import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import ModelPreparingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> satge {STAGE_NAME} started ")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> satge {STAGE_NAME} completed ")
    
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "preparing base models"
try:
    logger.info(f">>>>> satge {STAGE_NAME} started ")
    prepare_base_model= ModelPreparingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> satge {STAGE_NAME} completed ")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Training"
try:
    logger.info(f">>>>> satge {STAGE_NAME} started ")
    obj= ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> satge {STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e