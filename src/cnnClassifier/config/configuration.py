from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml,create_directory
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
     config_filepath=CONFIG_FILE_PATH,
     param_filepath=PARAM_FILE_PATH):
     self.config = read_yaml(config_filepath)
     self.param = read_yaml(param_filepath)

     create_directory([self.config.artifacts_root])

    def get_data_ingestion_configuration(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directory([config.root_dir])
        data_ingestion= DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            Unzip_dir=config.Unzip_zar)

        return data_ingestion