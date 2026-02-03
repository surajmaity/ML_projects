from dataclasses import field
import pickle
from fastapi import FastAPI
from fastapi.routing import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated


#import the ml model
with open('/Users/surajmaity/ML_projects/FastAPI_app/model.pkl','rb') as f:
    model = pickle.load(f)


app = FastAPI()

class UserInput(BaseModel):
    experience: float = Field(..., gt=0, lt=45, description='Experience of the user in years')


from fastapi import Body
import pandas as pd

@app.post('/predict')
def predict_salary(data: UserInput = Body(...)):
    """
    Receives user experience as input via UserInput Pydantic model.
    Constructs a DataFrame in the expected format for the ML model.
    Makes a prediction using the loaded model and returns the result.
    """

    # Convert the incoming pydantic model (user input) to a DataFrame. Model was trained with "YearsExperience" column.
    input_df = pd.DataFrame([{
        "YearsExperience": data.experience
    }])

    # Predict using the loaded model. The model's predict method returns an array, so we get the first value.
    prediction = model.predict(input_df)[0]

    # Return the prediction as a JSON response
    return JSONResponse(status_code=200, content={'predicted_salary': prediction})

# Explanation:
# 1. The endpoint receives a POST request at '/predict' with a JSON body containing "experience".
# 2. The data is parsed into the UserInput model, which validates that "experience" is a float between 0 and 45.
# 3. We build a pandas DataFrame from the validated input, as expected by the trained ML model.
# 4. The model predicts a salary based on the input experience value.
# 5. The predicted salary value is returned in JSON format to the client.
