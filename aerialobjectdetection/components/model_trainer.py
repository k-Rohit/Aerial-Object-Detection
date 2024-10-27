import os,sys
import yaml
import subprocess
from aerialobjectdetection.utils.main_utils import read_yaml_file
from aerialobjectdetection.logger import logging
from aerialobjectdetection.exception import AppException
from aerialobjectdetection.entity.config_entity import ModelTrainerConfig
from aerialobjectdetection.entity.artifacts_entity import ModelTrainingArtifact
from ultralytics import YOLO


class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig
    ):
        self.model_trainer_config = model_trainer_config
    
    def initiate_model_trainer(self) -> ModelTrainingArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        
        try:
            logging.info("Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
            os.chdir("YOLOv8Dataset")
            
            logging.info(f"Currently in directory {os.getcwd()}")
        
            new_train_path = "/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/YOLOv8Dataset/train"
            new_val_path = "/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/YOLOv8Dataset/val"
            
            with open("dataset.yaml", 'r') as file:
                dataset_config = yaml.safe_load(file)
            
            dataset_config['train'] = new_train_path
            dataset_config['val'] = new_val_path
            
            with open("dataset.yaml", 'w') as file:
                yaml.dump(dataset_config, file)
            
            logging.info(f"Updated dataset.yaml paths successfully. New train path: {new_train_path}, New val path: {new_val_path}")
        
        except Exception as e:
            raise AppException(f"Failed to update dataset.yaml: {str(e)}", sys)

        try:
            logging.info("Entering subprocess for training")
            yolo_model = YOLO("yolov8n.pt")
            logging.info("Starting Training")
            results = yolo_model.train(data="dataset.yaml",epochs=5, imgsz=640, batch=8)
            
            logging.info("Training completed")
            # After training, save model path in artifact
            model_trainer_artifact = ModelTrainingArtifact(trained_model_file_path="best.pt")
            
            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        
        except Exception as e:
            raise AppException(f"Failed during training subprocess: {str(e)}", sys)
