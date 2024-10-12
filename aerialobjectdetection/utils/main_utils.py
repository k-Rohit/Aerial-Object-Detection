import os.path
import sys
import yaml
import base64

from aerialobjectdetection.exception import AppException
from aerialobjectdetection.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e
        
    
    