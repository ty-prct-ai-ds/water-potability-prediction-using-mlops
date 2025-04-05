from fastapi import FastAPI
import pickle   
import pandas as pd
from data_model import Water

app = FastAPI(
    title="Water Potability Prediction API",
    description="API for predicting water potability using a trained model.",
)

with open("D:\Code\TY\MLops\water-potability-prediction-using-mlops\model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Water Potability Prediction API!"}

@app.post("/predict")
def predict_potability(water: Water):
    sample = pd.DataFrame({
        "ph": [water.ph],
        "Hardness": [water.Hardness],
        "Solids": [water.Solids],
        "Chloramines": [water.Chloramines],
        "Sulfate": [water.Sulfate],
        "Conductivity": [water.Conductivity],
        "Organic_carbon": [water.Organic_carbon],
        "Trihalomethanes": [water.Trihalomethanes],
        "Turbidity": [water.Turbidity]
    })

    predicted_value = model.predict(sample)

    if predicted_value == 1:
        return "Water is Consumable"
    else:
        return "Water is Not Consumable"