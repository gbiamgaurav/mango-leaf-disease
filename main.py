
from mango_leaf_disease import logger
from mango_leaf_disease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mango_leaf_disease.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from mango_leaf_disease.pipeline.stage_03_training import ModelTrainingPipeline
from mango_leaf_disease.pipeline.stage_04_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<") 
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training Stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation Stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e