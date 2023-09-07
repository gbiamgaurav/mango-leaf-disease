
from mango_leaf_disease.config.configuration import ConfigurationManager
from mango_leaf_disease.components.model_evaluation import Evaluation
from mango_leaf_disease import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(config = val_config)
        evaluation.evaluation()
        evaluation.save_score()