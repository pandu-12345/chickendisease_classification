import os
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directory
from cnnClassifier.entity.config_entity import (CallBackConfig, DataIngestionConfig, Evaluationconfig, ModelTrainingConfig,PrepareBaseModelConfig)


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
    
    def get_callback_config(self)->CallBackConfig:
        config=self.config.prepare_callback
        model_ckpt_dir= os.path.dirname(config.checkpoint_model_filepath)
        create_directory([model_ckpt_dir
                          ])

        callback_config= CallBackConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return callback_config
    
    def get_training_config(self)->ModelTrainingConfig:
        training=self.config.training
        params= self.param
        prepare_base_model= self.config.prepare_base_model

        training_data= os.path.join(self.config.data_ingestion.unzip_zar,"Chicken-fecal-images")

        create_directory([Path(training.root_dir)])

        model_trainig_config= ModelTrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(self.config.prepare_base_model.update_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_batch_size=params.BATCH_SIZE
        )
        return model_trainig_config
    

    def get_evaluation_configuration(self)->Evaluationconfig:
        config=self.config.data_ingestion
        create_directory([config.root_dir])
        evaluation_config= Evaluationconfig(
           path_of_model= Path("artifacts/training/model.keras"),
           training_data= Path("artifacts/data_ingestion/Chicken-fecal-images"),
           all_params= self.param,
           params_image_size=self.param.IMAGE_SIZE,
           params_batch_size=self.param.BATCH_SIZE,
            )

        return evaluation_config
    
    

    