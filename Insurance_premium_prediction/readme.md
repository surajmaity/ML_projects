# Insurance Premium Prediction API

A FastAPI-based machine learning service that predicts insurance premium categories based on user demographics, lifestyle factors, and location data.

## Features

- **ML-Powered Predictions**: Uses a trained machine learning model to predict insurance premium categories
- **Comprehensive Input Validation**: Pydantic models ensure data integrity and type safety
- **Derived Feature Engineering**: Automatically computes BMI, age groups, lifestyle risk, and city tiers
- **Confidence Scores**: Returns prediction confidence and probability distribution across all classes
- **RESTful API**: Clean, well-documented endpoints with proper error handling
- **Health Monitoring**: Built-in health check endpoint for service monitoring

## Project Structure

```
Insurance_premium_prediction/
├── app.py                      # FastAPI application and route handlers
├── model/
│   ├── model.pkl              # Trained ML model (pickle file)
│   └── predict.py             # Prediction logic and model loading
├── schema/
│   ├── user_input.py          # Pydantic model for input validation
│   └── prediction_response.py # Pydantic model for response structure
├── config/
│   └── city_tier.py           # City tier classification configuration
└── requirements.txt           # Python dependencies
```

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the Server

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### 1. Home Endpoint
**GET** `/`

Returns a welcome message.

**Response:**
```json
{
  "message": "Insurance premium prediction API"
}
```

### 2. Health Check
**GET** `/health`

Returns the API status, model version, and model loading status.

**Response:**
```json
{
  "status": "OK",
  "version": "1.0.0",
  "model_loaded": true
}
```

### 3. Predict Premium
**POST** `/predict`

Predicts the insurance premium category based on user input.

**Request Body:**
```json
{
  "age": 35,
  "weight": 75.5,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "predicted_category": "Medium",
  "confidence": 0.8432,
  "class_probabilities": {
    "Low": 0.01,
    "Medium": 0.15,
    "High": 0.84
  }
}
```

## Input Parameters

| Parameter | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| `age` | integer | Age of the user | 0 < age < 120 |
| `weight` | float | Weight in kg | weight > 0 |
| `height` | float | Height in meters | 0 < height < 2.5 |
| `income_lpa` | float | Annual salary in LPA (Lakhs Per Annum) | income_lpa > 0 |
| `smoker` | boolean | Whether the user is a smoker | true/false |
| `city` | string | City name | Any valid city name (normalized to Title Case) |
| `occupation` | string | Occupation type | One of: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job` |

## Derived Features

The API automatically computes the following features from the input:

- **BMI**: Calculated as `weight / (height²)`
- **Age Group**: Categorized as `young` (<25), `adult` (25-44), `middle_aged` (45-59), or `senior` (≥60)
- **Lifestyle Risk**: 
  - `high`: Smoker with BMI > 30
  - `medium`: Smoker OR BMI > 27
  - `low`: Otherwise
- **City Tier**: 
  - Tier 1: Major metropolitan cities (Mumbai, Delhi, Bangalore, etc.)
  - Tier 2: Secondary cities (Jaipur, Chandigarh, Indore, etc.)
  - Tier 3: All other cities

## Model Information

- **Model Version**: 1.0.0
- **Model Format**: Pickle (.pkl)
- **Model Location**: `/model/model.pkl`

## Error Handling

The API includes comprehensive error handling:
- **Validation Errors**: Returns 422 status code with detailed validation messages
- **Server Errors**: Returns 500 status code with error details
- **Input Validation**: All inputs are validated using Pydantic models before processing

## Example Usage with cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "weight": 75.5,
    "height": 1.75,
    "income_lpa": 12.5,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }'
```

## Example Usage with Python

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "age": 35,
    "weight": 75.5,
    "height": 1.75,
    "income_lpa": 12.5,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

response = requests.post(url, json=data)
print(response.json())
```

## Development

### Key Technologies

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Pandas**: Data manipulation and DataFrame operations
- **Pickle**: Model serialization and loading

### Code Structure

- **`app.py`**: Main FastAPI application with route definitions
- **`model/predict.py`**: Model loading and prediction logic
- **`schema/user_input.py`**: Input validation schema with computed fields
- **`schema/prediction_response.py`**: Response structure definition
- **`config/city_tier.py`**: City tier classification configuration

## Notes

- Ensure the model file (`model.pkl`) exists in the `model/` directory before running the API
- The model path in `predict.py` uses an absolute path - consider using relative paths or environment variables for production deployments
- City names are automatically normalized (trimmed and converted to Title Case)

## License

[Add your license information here]

## Author

[Add your name/contact information here]
