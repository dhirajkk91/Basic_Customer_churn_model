# Customer Churn Prediction

This repository contains a Jupyter notebook and a packaged Keras/TFLite customer churn model. The project also includes a small FastAPI server and a Dockerfile so you can run the model as a local service or inside a container.

Contents

- `Customer_churn_prediction.ipynb` — training and conversion notebook
- `my_model_package/` — packaged model code and bundled model files
- `churn_model.h5` — Keras HDF5 model (now included inside `my_model_package/`)
- `model_churn.tflite` — TFLite model (included inside `my_model_package/`)
- `app.py` — FastAPI server that serves the model
- `Dockerfile` — container image definition
- `requirements.txt` — Python dependencies

Quick start (local)

1. (Optional) Create and activate a virtualenv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the FastAPI server:

```powershell
uvicorn app:app --host 0.0.0.0 --port 8000
```

4. Test endpoints:

```powershell
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"features": [/* numeric features */]}'
```

Building and running with Docker

1. Build the Docker image (from repo root):

```powershell
docker build -t churn_model_image .
```

2. Run the container:

```powershell
docker run -d -p 80:80 churn_model_image
```

3. Test the service (same endpoints as above, default port 80 in container):

```powershell
curl http://localhost/health
curl -X POST http://localhost/predict -H "Content-Type: application/json" -d '{"features": [/* numeric features */]}'
```

Notes and recommendations

- Docker images that include TensorFlow can be large. To reduce image size you can:
  - Use a smaller TF runtime (e.g. `tensorflow-cpu`),
  - Use multi-stage builds, or
  - Host model artifacts externally and download them during image build or at runtime.
- If you plan to publish multiple model versions, consider using Git LFS or storing the models on cloud storage and referencing them instead of committing binaries into Git.

If you want, I can: add a TFLite-based inference endpoint, add Git LFS configuration, or prepare a `docker-compose.yml` file for local testing. Tell me which you'd prefer.
# Customer Churn Prediction

This project contains a Jupyter notebook `Customer_churn_prediction.ipynb` that trains a Keras model for customer churn and converts it to TFLite.

Included artifacts

- `Customer_churn_prediction.ipynb` — training and conversion notebook
- `churn_model.h5` — Keras HDF5 model exported from the notebook
- `model_churn.tflite` — TFLite model converted from the SavedModel/HDF5
- `saved_model_churn/` — SavedModel directory 

Quick use

1. To run the notebook interactively, open `Customer_churn_prediction.ipynb` in Jupyter and run cells in order.
2. To load the provided Keras model in Python:

```python
from tensorflow import keras
model = keras.models.load_model('churn_model.h5')
```

3. To test the TFLite model locally, use the TFLite Interpreter (example):

```python
import tensorflow as tf
interpreter = tf.lite.Interpreter(model_path='model_churn.tflite')
interpreter.allocate_tensors()
# set inputs / run inference as needed
```




