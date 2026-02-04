## FastAPI Salary Prediction App

This project exposes a **salary prediction** machine learning model via a FastAPI backend, with a simple **Streamlit** frontend for interaction.

The model is loaded from `model.pkl` and expects a single feature: **years of experience**. It returns a predicted salary.

---

### Project structure

- `main.py` – FastAPI backend that:
  - loads the trained model from `model.pkl`
  - defines the `UserInput` Pydantic model
  - exposes the `/predict` POST endpoint
- `Frontend.py` – Streamlit app that:
  - lets the user input years of experience
  - calls the FastAPI `/predict` endpoint
  - displays the predicted salary
- `model.pkl` – pickled regression model trained on the salary dataset
- `Salary_dataset.csv` – original training data (not used at runtime)

---

### Requirements

You will need Python 3.9+ and the following packages (install them into a virtual environment if possible):

```bash
pip install fastapi uvicorn[standard] pydantic pandas scikit-learn streamlit requests
```

If additional dependencies were used during training, install them as well.

---

### Running the FastAPI backend

From the `FastAPI_app` directory:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

This will start the API server at `http://localhost:8000`.

You can verify the API is running by opening the automatic docs:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

### `/predict` API endpoint

- **URL**: `POST /predict`
- **Content-Type**: `application/json`
- **Request body schema**:

```json
{
  "experience": 5.0
}
```

- **Rules**:
  - `experience` must be a float
  - `0 < experience < 45` (validated by Pydantic)

- **Successful response (HTTP 200)**:

```json
{
  "predicted_salary": 65000.0
}
```

If the payload is invalid (e.g., missing field, out-of-range value), FastAPI will return a **422 Unprocessable Entity** error with details.

---

### Running the Streamlit frontend

With the FastAPI server already running on `http://localhost:8000`, start Streamlit from the same directory:

```bash
streamlit run Frontend.py
```

Then open the URL shown in the terminal (typically `http://localhost:8501`).

The app will:

- ask for **Years of Experience**
- send a POST request to `http://localhost:8000/predict`
- display the **Predicted Salary** returned by the backend

If you run the backend on a different host/port, update the `api_url` in `Frontend.py` accordingly.

---

### Notes

- Make sure `model.pkl` is present in the `FastAPI_app` directory and compatible with the code in `main.py` (expects a model with a `.predict()` method that accepts a pandas `DataFrame` with a `YearsExperience` column).
- For deployment, consider:
  - serving FastAPI with a production server (e.g., `gunicorn` + `uvicorn.workers.UvicornWorker`)
  - putting Streamlit or any other UI behind a reverse proxy
  - configuring CORS if the frontend is hosted on a different domain.
