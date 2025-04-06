from src.Project1.config.configuration import ConfigurationManager
from src.Project1.components.data_ingestion import DataIngestion
from src.Project1 import logger

STAGE_NAME = "Data Ingestion Stage"

class  DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self): 
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion  = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
    except Exception as e:
        logger.exception(e)
