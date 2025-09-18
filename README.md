**Customer Churn Prediction — Compact Deployable Project**

This repository is a concise, end-to-end example demonstrating how to train, package, and serve a Keras customer-churn model. It's optimized for clarity, reproducibility, and fast evaluation by reviewers.

Why this project is valuable
- Shows end-to-end ML lifecycle from data preprocessing to model training, conversion, packaging, and deployment.
- Demonstrates clean Python packaging, a minimal FastAPI inference service, and a Docker container suitable for staging.

Files:
- `Customer_churn_prediction.ipynb`: clear, well-commented notebook for data prep and model training.
- `my_model_package/`: self-contained package with model artifacts and loader utilities.
- `app.py`: minimal FastAPI app exposing `/health` and `/predict` endpoints with startup model-loading and input validation.
- `Dockerfile` and `requirements.txt`: reproducible environment and container instructions.

Quick evaluation checklist (run in order)
1. Clone the repository and change into the project directory.

```powershell
git clone https://github.com/dhirajkk91/Basic_Customer_churn_model.git
cd Basic_Customer_churn_model
```

2. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install Python dependencies.

```powershell
pip install -r requirements.txt
```

4. Run the API locally:

```powershell
uvicorn app:app --host 0.0.0.0 --port 8000
```

Notes 
- Model artifacts are included for quick evaluation; for production these should be served from an artifact store or via CI-promoted releases.
- The project intentionally balances clarity and deployability: it uses TensorFlow for model training but can be switched to TFLite for a smaller runtime footprint.

Contact
- Author: Dhiraj Karki 
- Email: dhirajkk91@gmail.com



