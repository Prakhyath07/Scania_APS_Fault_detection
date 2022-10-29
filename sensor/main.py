# from sensor.configuration.mongodb_connection import MongoDBClient

# if __name__ == '__main__':
#     mongodb_client = MongoDBClient()
#     print(mongodb_client.database.list_collection_names())


# import os,sys

# from sensor.exception import SensorException

# def test_exception():
#     try:
#         x=1/0

#     except Exception as e:
#         raise SensorException(e,sys)

# if __name__ == "__main__":
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)