import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "src")))
from cnnClassifier.loggs import  logger
from cnnClassifier.config.configuration import  ConfigurationManager
from cnnClassifier.entity.config_entity import  PrepareBaseModelConfig
from cnnClassifier.components.models import PrepareBaseModel



STAGE_NAME = "preparing base models"

class ModelPreparingPipeline:
    def __init__(self):
        pass

    def main(self):
        configmanager=ConfigurationManager()
        prepare_base_model_config=configmanager.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f">>>>> satge {STAGE_NAME} started ")
        obj= ModelPreparingPipeline()
        obj.main()
        logger.info(f">>>>> satge {STAGE_NAME} completed ")
    except Exception as e:
        logger.exception(e)
        raise e