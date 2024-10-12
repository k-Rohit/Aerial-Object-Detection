ARTIFACTS_DIR: str = "artifacts"

'''
Data Ingestion related constant start with DATA_INGESTION VAR_NAME

'''

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/17jLfOPqRV3pbh0yvaPHarfaUSOeyFmFZ/view?usp=sharing"


'''
Data Valiadtion related constants 

'''

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "val", "dataset.yaml"]

'''
Model Training related constant start with MODEL_TRAINER var name

'''

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT: str = "yolov8s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 100
MODEL_TRAINER_BATCH_size: int = 8