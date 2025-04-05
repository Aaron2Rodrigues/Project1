from src.Project1.config.configuration import ConfigurationManager
from src.Project1.components.data_transformation import DataTransformation
from src.Project1 import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransormationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.train_test_splitting()

if __name__ == '__main__':
    try:
        with open(Path('artifacts/data_validation/status.txt'),'r') as f:
             status = f.read().split(" ")[-1]
        if status == "True":
            logger.info("Data Transformation is successful")
            logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
            obj = DataTransormationTrainingPipeline()
            obj.initiate_data_transformation()()
            logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
        else:
            raise Exception("Data Validation is not successful")
    
    except Exception as e:
        logger.exception(e)
        raise e
