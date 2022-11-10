from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.pipeline.prediction_pipeline import PredictPipeline
import os
from sensor.utils.main_utils import read_yaml_file
from sensor.constants.training_pipeline import SAVED_MODEL_DIR
from fastapi import FastAPI, UploadFile
from sensor.constants.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import pandas as pd
import os




env_file_path=os.path.join(os.getcwd(),"env.yaml")

# def set_env_variable(env_file_path):

#     if os.getenv('MONGO_DB_URL',None) is None:
#         env_config = read_yaml_file(env_file_path)
#         os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:

        train_pipeline = TrainPipeline()
        if TrainPipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

class results(BaseModel):
    idx : int
    prediction: str

@app.post("/predict",response_model=List[results])
async def predict_route(file: UploadFile):
    try:
        
        #get data from user csv file
        #conver csv file to dataframe
        cont =await file.read()
        predictpipeline =PredictPipeline(cont)
        #decide how to return file to user.
        pred_artifact = predictpipeline.run_pipeline()
        df = pd.read_csv(pred_artifact.prediction_file_path)
        a= [results(idx = i, prediction=df.iloc[i,-1]) for i in range(df.shape[0])]
        print(a)
        return a
        
    except Exception as e:
        raise Response(e)

def main():
    try:
        # set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
        
    except Exception as e:
        TrainPipeline.is_pipeline_running = False
        print(e)
        logging.exception(e)


if __name__=="__main__":
    #main()
    # set_env_variable(env_file_path)
    app_run(app, host=APP_HOST, port=APP_PORT)