from Chronic_Kidney_cnnClassifier import logger
from Chronic_Kidney_cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chronic_Kidney_cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chronic_Kidney_cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from Chronic_Kidney_cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
import os



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Evaluation stage"
try:
  
   # Connect Daghub and ML-Flow
   os.environ["MLFLOW_TRACKING_URI"]="<DagsHub URL>"
   os.environ["MLFLOW_TRACKING_USERNAME"]="<User name>"
   os.environ["MLFLOW_TRACKING_PASSWORD"]="<DagsHub Password>"
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e


