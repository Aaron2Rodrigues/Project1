from src.Project1.config.configuration import ConfigurationManager
from src.Project1.components.model_trainer import ModelTrainer
from src.Project1 import logger

STAGE_NAME = "Model Trainer Stage"
class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train() 

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e 