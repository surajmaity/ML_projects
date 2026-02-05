from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import MODEL_VERSION, predict_output,model
from schema.prediction_response import PredictionResponse


app = FastAPI()



#human readable
@app.get('/')
def home():
    return JSONResponse(content={'message': 'Insurance premium prediction API'})


#machine readable
@app.get('/health')
def health_check():
    return {
        'status' : 'OK',
        'version' : MODEL_VERSION,
        'model_loaded' : model is not None
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }


    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})


    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))





