import os,sys
import yaml
from aerialobjectdetection.utils.main_utils import read_yaml_file
from aerialobjectdetection.logger import logging
from aerialobjectdetection.exception import AppException
from aerialobjectdetection.entity.config_entity import ModelTrainerConfig
from aerialobjectdetection.entity.artifacts_entity import ModelTrainingArtifact

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig
    ):
        self.model_trainer_config = model_trainer_config