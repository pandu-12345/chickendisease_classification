from  src.cnnClassifier.loggs import  logger
from  src.cnnClassifier.config.configuration import  ModelconfigurationManager
from  src.cnnClassifier.entity.config_entity import  PrepareBaseModelConfig
from src.cnnClassifier.components.models import PrepareBaseModel




STAGE_NAME = "preparing base models"

class ModelPreparingPipline:
    def __init__(self):
        pass

    def main(self):
        configmanager=ModelconfigurationManager()
        prepare_base_model_config=configmanager.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f">>>>> satge {STAGE_NAME} started ")
        obj= ModelPreparingPipline()
        obj.main()
        logger.info(f">>>>> satge {STAGE_NAME} completed ")
    except Exception as e:
        logger.exception(e)
        raise e