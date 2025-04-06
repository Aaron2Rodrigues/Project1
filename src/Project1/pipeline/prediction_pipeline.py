import joblib
import numpy as np 
import pandas as pd
import pathlib as Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts\model_trainer\model.joblib")

    def predict(self,data):
        predictions = self.model.predict(data)

        return predictions
