from fastapi import FastAPI
import pandas as pd 
from fastapi.responses import JSONResponse
from schema.user_input import person
from schema.user_input import prediction_response
from model.predict import predict_primium, MODEL_VERSION,model
import pickle
app = FastAPI()


@app.get("/home")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

@app.get("/health")
def health_check():
    return {"status": "OK",
            "model_version": MODEL_VERSION,
            "model_loaded": model is not None}



@app.post("/predict_primium/", response_model=prediction_response)
def predict_premium_endpoint(data:person):
    # income_lpa	occupation	insurance_premium_category	bmi	age_group	life_risk	tier_city
    input={ "income_lpa":[data.income_lpa],
                         "occupation":[data.occupation],
                         "bmi":[data.bmi],
                            "age_group":[data.age_group],
                            "life_risk":[data.life_risk],
                            "tier_city":[data.city_tier]

                        }
    try:
       result=predict_primium(input)
       return JSONResponse(content={
           "predicted_insurance_premium": result["prediction"],
           "class_probabilities": result["probabilities"]
       },status_code=200)
    except Exception as e:
       return JSONResponse(content={"error": str(e)}, status_code=500)