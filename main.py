from src.Project1.components import data_ingestion
from src.Project1 import logger
from src.Project1.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Project1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Project1.pipeline.data_transformation_pipeline import DataTransormationTrainingPipeline
from src.Project1.pipeline.model_trianer_pipeline import ModelTrainerPipeline
from src.Project1.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
  logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
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
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<\n\nx===================================x")
except Exception as e:
        logger.exception(e)
        raise e
STAGE_NAME = "Data Transformation Stage"

try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<\n\n\nx===================================x")
        obj = DataTransormationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<\n\n\nx===================================x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer Stage"

try:  
      logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<\n\n\nx===================================x")
      obj = ModelTrainerPipeline()
      obj.initiate_model_training()
      logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<\n\n\nx===================================x")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Model Evaluation Stage"
try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<\n\n\nx===================================x")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<\n\n\nx===================================x")
except Exception as e:
        logger.exception(e)
        raise e 