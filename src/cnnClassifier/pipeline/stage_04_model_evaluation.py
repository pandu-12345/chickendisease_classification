import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "src")))

from  cnnClassifier.loggs import  logger
from cnnClassifier.components.model_evalution import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager



STAGE_NAME = "Model EVALUATION"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        evaluation_config = config_manager.get_evaluation_configuration()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> satge {STAGE_NAME} started ")
        obj= EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> satge {STAGE_NAME} completed ")
    except Exception as e:
        logger.exception(e)
        raise e