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





