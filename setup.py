from setuptools import setup, find_packages

setup(
    name='my_model_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={'my_model_package': ['churn_model.h5', 'model_churn.tflite']},
    install_requires=[
        'tensorflow==2.6.0',
        'pandas==1.3.3',
        'numpy==1.21.2',
        'scikit-learn==0.24.2'
    ],
    description='A packaged customer churn model (Keras + TFLite)'
)
