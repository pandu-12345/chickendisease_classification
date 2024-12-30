from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml,create_directory
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig)


class DataIngestionConfigurationManager:
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


class ModelconfigurationManager:
    def __init__(self,
     config_filepath=CONFIG_FILE_PATH,
     param_filepath=PARAM_FILE_PATH):
     self.config = read_yaml(config_filepath)
     self.param = read_yaml(param_filepath)
    
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config=self.config.prepare_base_model
        params= self.param
        create_directory([config.root_dir])
        
        prepare_base_model= PrepareBaseModelConfig(
            root_dir= Path(config.root_dir),
            base_model= Path(config.base_model_path),
            update_base_model= Path(config.update_base_model_path),
            Params_image_size=params.IMAGE_SIZE,
            Params_learning_rate=params.LEARNING_RATE,
            Params_batch_size=params.BATCH_SIZE,
            Params_includetop=params.INCLUDE_TOP,
            Params_weights=params.WEIGHETS,
            Params_class=params.CLASSES,
        )
        return prepare_base_model