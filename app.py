from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import logging
from my_model_package import load_keras_model

app = FastAPI()
logger = logging.getLogger("uvicorn.error")


class PredictRequest(BaseModel):
    features: list


@app.on_event("startup")
def startup_event():
    try:
        app.state.model = load_keras_model()
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.exception("Failed to load model at startup: %s", e)
        app.state.model = None


@app.get('/health')
def health():
    ready = app.state.model is not None
    return {'status': 'ok', 'ready': ready}


@app.post('/predict')
def predict(req: PredictRequest):
    if app.state.model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    try:
        x = np.array(req.features, dtype=float)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid features: must be a numeric list")

    if x.ndim == 1:
        x = x.reshape(1, -1)

    try:
        pred = app.state.model.predict(x)
        prob = float(pred.squeeze())
    except Exception as e:
        logger.exception("Prediction failed: %s", e)
        raise HTTPException(status_code=500, detail="Prediction failed")

    return {'probability': prob}
