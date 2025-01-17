from  cnnClassifier.config.configuration import  ConfigurationManager
from  cnnClassifier.loggs import  logger
from cnnClassifier.components.training import Training
from cnnClassifier.components.prepare_callbacks import preparecallback

STAGE_NAME= "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_callBacks_config= config.get_callback_config()
        prepare_Callbacks= preparecallback(config=prepare_callBacks_config)
        callback_list= prepare_Callbacks.get_tb_ckpt_callback()

        training_Config= config.get_training_config()
        training= Training(config= training_Config)
        training.get_base_model()
        training.train_valid_genrator()
        training.train(callback_list= callback_list)


if __name__ == '__main__':
    try:
        logger.info(f">>>>> satge {STAGE_NAME} started ")
        obj= ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> satge {STAGE_NAME} completed ")
    except Exception as e:
        logger.exception(e)
        raise e