# import os,sys
# import yaml
# import subprocess
# from aerialobjectdetection.utils.main_utils import read_yaml_file
# from aerialobjectdetection.logger import logging
# from aerialobjectdetection.exception import AppException
# from aerialobjectdetection.entity.config_entity import ModelTrainerConfig
# from aerialobjectdetection.entity.artifacts_entity import ModelTrainingArtifact
# from ultralytics import YOLO

# source_path = "YOLOv8Dataset/runs/detect/train/weights/best.pt"
# destination_path = "models/best.pt"
# class ModelTrainer:
#     def __init__(
#         self,
#         model_trainer_config: ModelTrainerConfig
#     ):
#         self.model_trainer_config = model_trainer_config
    
#     def initiate_model_trainer(self) -> ModelTrainingArtifact:
#         logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        
#         try:
#             logging.info("Unzipping data")
#             os.system("unzip data.zip")
#             os.system("rm data.zip")
#             os.chdir("YOLOv8Dataset")
            
#             logging.info(f"Currently in directory {os.getcwd()}")
        
#             new_train_path = "/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/YOLOv8Dataset/train"
#             new_val_path = "/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/YOLOv8Dataset/val"
            
#             with open("dataset.yaml", 'r') as file:
#                 dataset_config = yaml.safe_load(file)
            
#             dataset_config['train'] = new_train_path
#             dataset_config['val'] = new_val_path
            
#             with open("dataset.yaml", 'w') as file:
#                 yaml.dump(dataset_config, file)
            
#             logging.info(f"Updated dataset.yaml paths successfully. New train path: {new_train_path}, New val path: {new_val_path}")
        
#         except Exception as e:
#             raise AppException(f"Failed to update dataset.yaml: {str(e)}", sys)

#         try:
#             logging.info("Entering subprocess for training")
#             yolo_model = YOLO("yolov8n.pt")
#             logging.info("Starting Training")
#             results = yolo_model.train(data="dataset.yaml",epochs=5, imgsz=640, batch=8)
            
#             logging.info("Training completed")
#             try:
#                 # Move the file
#                 shutil.move(source_path, destination_path)
#                 print(f"Moved best.pt to {destination_path}")
#             except FileNotFoundError as e:
#                 print(f"Error: {e}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
                        
#             # After training, save model path in artifact
#             model_trainer_artifact = ModelTrainingArtifact(trained_model_file_path="best.pt")
            
#             logging.info("Exited initiate_model_trainer method of ModelTrainer class")
#             logging.info(f"Model trainer artifact: {model_trainer_artifact}")
#             return model_trainer_artifact
        
#         except Exception as e:
#             raise AppException(f"Failed during training subprocess: {str(e)}", sys)



import os
import sys
import yaml
import shutil
import subprocess
from aerialobjectdetection.utils.main_utils import read_yaml_file
from aerialobjectdetection.logger import logging
from aerialobjectdetection.exception import AppException
from aerialobjectdetection.entity.config_entity import ModelTrainerConfig
from aerialobjectdetection.entity.artifacts_entity import ModelTrainingArtifact
from ultralytics import YOLO

source_path = "YOLOv8Dataset/runs/detect/train/weights/best.pt"
runs_folder = "Aerial-Object-Detection/YOLOv8Dataset"
destination_path = "models/best.pt"
root_dir = 'Aerial-Object-Detection'


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config
    
    def initiate_model_trainer(self) -> ModelTrainingArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        
        try:
            # Unzip and prepare dataset
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
            # Train the model
            logging.info("Entering subprocess for training")
            yolo_model = YOLO("yolov8n.pt")
            logging.info("Starting Training")
            results = yolo_model.train(data="dataset.yaml", epochs=5, imgsz=640, batch=8)
            
            logging.info("Training completed")

            # Move best.pt and runs folder after training
            if os.path.exists(source_path):
                try:
                    shutil.move(source_path, destination_path)
                    logging.info(f"Moved best.pt to {destination_path}")
                except Exception as e:
                    logging.error(f"Failed to move best.pt: {str(e)}")
                    raise AppException(f"Failed to move best.pt: {str(e)}", sys)
            else:
                logging.error("best.pt file not found after training.")
                raise AppException("best.pt file not found after training.", sys)
            
            if os.path.exists(runs_folder):
                try:
                    # Construct the destination path for the runs folder in the root directory
                    destination_runs_path = os.path.join(root_dir, 'runs')
                    shutil.move(runs_folder, destination_runs_path)
                    # shutil.remove("YOLOv8Dataset")
                    logging.info(f"Runs folder moved to {destination_runs_path}")
                except Exception as e:
                    logging.error(f"Failed to move runs folder: {str(e)}")
                    raise AppException(f"Failed to move runs folder: {str(e)}", sys)
            else:
                logging.error("Runs folder not found after training.")
                raise AppException("Runs folder not found after training.", sys)
            
            # Save model path in artifact
            model_trainer_artifact = ModelTrainingArtifact(trained_model_file_path=destination_path)
            
            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        
        except Exception as e:
            raise AppException(f"Failed during training subprocess: {str(e)}", sys)
