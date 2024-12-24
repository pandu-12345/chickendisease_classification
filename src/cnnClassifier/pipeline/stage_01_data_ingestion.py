
from  src.cnnClassifier.loggs import  logger
from  src.cnnClassifier.config.configuration import  ConfigurationManager
from  src.cnnClassifier.entity.config_entity import  DataIngestionConfig
from src.cnnClassifier.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        data_config=  config.get_data_ingestion_configuration()
        data_ingestion= DataIngestion(data_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()



if __name__ == '__main__':
    try:
        logger.info(f">>>>> satge {STAGE_NAME} started ")
        obj= DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>>>> satge {STAGE_NAME} completed ")
    except Exception as e:
        logger.exception(e)
        raise e