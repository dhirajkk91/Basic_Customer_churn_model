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




