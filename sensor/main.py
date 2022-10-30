# from sensor.configuration.mongodb_connection import MongoDBClient

# if __name__ == '__main__':
#     mongodb_client = MongoDBClient()
#     print(mongodb_client.database.list_collection_names())


# import os,sys
# from sensor.logger import logging

# from sensor.exception import SensorException

# def test_exception():
#     try:
#         logging.info("divde by 0")
#         x=1/0
        


#     except Exception as e:
#         raise SensorException(e,sys)

# if __name__ == "__main__":
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)


# from sensor.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig

# if __name__ == "__main__":
#     try:
#         train = TrainingPipelineConfig()
#         data = DataIngestionConfig(train)
#         print(data.__dict__)
#     except Exception as e:
#         print(e)

from sensor.pipeline.training_pipeline import TrainPipeline
if __name__ == "__main__":
    try:
        TrainPipeline().run_pipeline()
    except Exception as e:
        print(e)