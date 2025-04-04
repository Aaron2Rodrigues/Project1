from logging import config
from src.Project1.config.configuration import ConfigurationManager
from src.Project1.components.data_validation import DataValidation
from src.Project1 import logger

STAGE_NAME = "Data Validation Stage"

class  DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config  = ConfigurationManager() 
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
