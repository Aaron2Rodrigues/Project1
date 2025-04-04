from src.Project1.components import data_ingestion
from src.Project1 import logger
from src.Project1.pipeline.data_ingestion_pipeline import DataIngestionTrainigPipeline
from src.Project1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
  logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
  data_ingestion = DataIngestionTrainigPipeline()
  data_ingestion.initiate_data_ingestion()
  logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e
