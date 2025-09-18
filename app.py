from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from my_model_package import load_keras_model, get_tflite_path

app = FastAPI()

class PredictRequest(BaseModel):
    features: list

# Load model once at startup
model = load_keras_model()

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def predict(req: PredictRequest):
    x = np.array(req.features)
    if x.ndim == 1:
        x = x.reshape(1, -1)
    pred = model.predict(x)
    prob = float(pred.squeeze())
    return {'probability': prob}
