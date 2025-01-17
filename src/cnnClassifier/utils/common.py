import os
from cnnClassifier.loggs import logger
import json
import joblib
from pathlib import Path
import yaml
from typing import Any
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import base64
from box import ConfigBox



def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def create_directory(path_to_directory:list , verbose=True):
    for direc in path_to_directory:
        os.makedirs(direc, exist_ok=True)
        if verbose:
            logger.info(f"Directory: {direc} created successfully")

def save_jason(path:Path, data:dict):
    with open(path, "w") as f:
        json.dump(data, f,indent=4)
    logger.info(f"Jason file: {path} saved successfully")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content= json.load(f)
    logger.info(f"json file loaded succefully from :{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(data, path)
    logger.info(f"Binary file saved successfully at :{path}")


@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f"Binary file loaded successfully from :{path}")

@ensure_annotations
def get_sizes(path:Path)->str:
    size_in_KB= round(os.pathgetsize(path)/1024)
    return f"{size_in_KB} KB"

def decodeImage(imagestring,filename):
    imgdata=base64.base64decode(imagestring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()



