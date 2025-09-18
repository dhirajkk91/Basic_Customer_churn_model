import os
from tensorflow import keras

PACKAGE_DIR = os.path.dirname(__file__)

def load_keras_model():
    path = os.path.join(PACKAGE_DIR, 'churn_model.h5')
    return keras.models.load_model(path)

def get_tflite_path():
    return os.path.join(PACKAGE_DIR, 'model_churn.tflite')
