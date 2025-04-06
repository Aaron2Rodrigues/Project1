from src.Project1.config.configuration import  ConfigurationManager
from src.Project1.components.model_evaluation import ModelEvaluation
from src.Project1 import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_eval_config  = config.get_model_evaluation_config()
        model_evaluation  = ModelEvaluation(config = model_eval_config)
        model_evaluation.log_into_mlflow()


if __name__ == '__main__':  
    try:
        logger.info(f">>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<")
    except Exception as e:
        raise e    