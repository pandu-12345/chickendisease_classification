import os
from urllib.request import urlretrieve
from  src.cnnClassifier.utils.common import get_sizes
from  src.cnnClassifier.loggs import  logger
import zipfile
from pathlib import Path
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        path= Path(self.config.local_data_file)
        if not path.exists():
            filename,headers= urlretrieve(
                url= self.config.source_URL,
                filename=str(path)
                )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        else :
            logger.info(f"file already exists of size : {get_sizes(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.Unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Zip file extracted to : {unzip_path}")