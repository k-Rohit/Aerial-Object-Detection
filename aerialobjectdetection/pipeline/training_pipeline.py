import sys, os
from aerialobjectdetection.logger import logging
from aerialobjectdetection.exception import AppException
from aerialobjectdetection.components.data_ingestion import DataIngestion
from aerialobjectdetection.components.data_validation import DataValidation
from aerialobjectdetection.components.model_trainer import ModelTrainer


from aerialobjectdetection.entity.config_entity import (DataIngestionConfig, 
                                                        DataValidationConfig,
                                                        ModelTrainerConfig)

from aerialobjectdetection.entity.artifacts_entity import (DataIngestionArtifact,
                                                           DataValidationArtifact,
                                                           ModelTrainingArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start data_ingestion method of the TrainPipeline class"
            )
            logging.info("Getting data from url")
            data_ingestion = DataIngestion(
                data_ingestion_config= self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got data from url")
            logging.info("Exited the data_ingestion method")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys)
        
    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        
        logging.info("Entered the start_data_validation method of TrainPipeline class")
        try:
            data_validation = DataValidation(data_ingestion_artifact = data_ingestion_artifact, 
                                             data_validation_config = self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Performed the data validation operation")
            
            logging.info("Performed the data validation operation")
            logging.info("Exited the start data_validation method of TrainPipeline class")
            
            return data_validation_artifact
        except Exception as e:
            raise AppException(e, sys)
        
    def start_model_trainer(self) -> ModelTrainingArtifact:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise AppException(e, sys)
        
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            model_trainer_artifact = self.start_model_trainer()
        
        except Exception as e:
            raise AppException(e, sys)
    
    