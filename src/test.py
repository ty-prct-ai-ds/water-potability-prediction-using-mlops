import json
import requests

url = "https://water-prediction-cloud.onrender.com/predict"

x_new = dict (
    ph = 7.4,
    Hardness = 200,
    Solids = 300,
    Chloramines = 10,
    Sulfate = 200,
    Conductivity = 400,
    Organic_carbon = 10,
    Trihalomethanes = 0.5,
    Turbidity = 5
)

x_new_json = json.dumps(x_new)

requests.post(url, data=x_new_json)

print(requests.post(url, data=x_new_json).text)
print(requests.post(url, data=x_new_json).status_code)