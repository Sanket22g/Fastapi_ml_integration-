
import pickle
import pandas as pd
import os

# Use relative path that works in Docker and locally
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Model version
MODEL_VERSION = "1.0.0"
#lets see probability as well

def predict_primium(input_data):

    input=pd.DataFrame(input_data)
    
    prediction=model.predict(input)[0]
    
    # Get class probabilities
    probabilities = model.predict_proba(input)[0]
    class_names = model.classes_
    
    # Create dict with class probabilities
    proba_dict = {str(class_name): float(prob) for class_name, prob in zip(class_names, probabilities)}

    return {
        "prediction": prediction,
        "probabilities": proba_dict
    }