import os 
import sys
from tabnanny import verbose
from  src.Project1 import logger
import yaml
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox, config_box
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    
    """
    Read yaml file and returns a ConfigBox object
    
    Args:
    path_to_yaml (Path): Path to the yaml file
    
    Returns:
    ConfigBox: ConfigBox object
    
    """
    try:

        with open(path_to_yaml) as yaml_file:
             content = yaml.safe_load(yaml_file)
             logger.info(f" Read yaml file from {path_to_yaml}")
             return ConfigBox(content)
    except BoxValueError:
         raise ValueError("Yaml file is empty")
    except Exception as e:
         raise e
    
@ensure_annotations
def create_dirs(dirs_list : list,verbose=True):
     
     """
     Create directories in the list if they do not exist
     
     Args:
     dirs_list (list): List of directories to create
     
     """
     for path in dirs_list:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory {path}")      

@ensure_annotations
def save_json(path: Path , data:dict):
     
     """
     Save json file
     
     Args:
     path (Path): Path to save the json file
     data (dict): Data to save in the json file
     """
     
     with open(path,'w') as f:
          json.dump(data,f,indent = 4)
          logger.info(f"Saved json file to {path}")

@ensure_annotations
def load_json(path: Path )-> ConfigBox:
     
     """
     Load Json file


     Args: 
     path(Path): Path to the json file


     Returns:
     ConfigBox: data as a class attribute instead of a dictionary
     """

     with open(path)as f:
          data = json.load(f)
          logger.info(f"Loaded json file from {path}")
          return ConfigBox(data)
     
@ensure_annotations
def save_bin(data: Any, path: Path) :
     
     """
     Save model

     Args:
     data(Any): Data to save
     path(Path): Path to save the model

     """

     joblib.dump(data,path)
     logger.info(f"Saved binary file to {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
     
     """
     Load the model 
     
     Args:
     path(Path): Path of the saved model
     
     Returns:
     Any: Loaded model

     """

     data = joblib.load(path)
     logger.info(f"Loaded binary file from {path}")
     return data