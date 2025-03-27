"""import os
import sys

# Set the working directory to the project root
current_file_path = os.path.abspath(__file__)  # Path to this script
project_root = os.path.abspath(os.path.join(os.path.dirname(current_file_path), "../../../.."))
os.chdir(project_root)  # Change the working directory to the project root

# Add project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

"""""
import os
import sys
sys.path.append(os.path.join(os.getcwd(), "src"))
# Add the parent directory of "myproject" to the system path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("Current Working Directory:", os.getcwd())

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.loggs import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
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
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> satge {STAGE_NAME} completed ")
    except Exception as e:
        logger.exception(e)
        raise e