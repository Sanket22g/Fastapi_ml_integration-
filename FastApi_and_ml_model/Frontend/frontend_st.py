import streamlit as st 
import requests
API_URL= "http://127.0.0.1:8000/predict_primium/"

st.title("Insurance Premium Prediction")
st.markdown("Enter the details below to predict the insurance premium category.")

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (in kgs)", min_value=1.0, max_value=500.0, value=70.0)
height = st.number_input("Height (in meters)", min_value=0.1, max_value=2.5, value=1.75)
income_lpa = st.number_input("Income (in lpa)", min_value=0.1, max_value=100.0, value=10.0)
smoker = st.selectbox("Smoker", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
city = st.selectbox("City", options=["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata", "Pune", "Chandigarh", "Lucknow", "Gaya", "Mysore", "Jalandhar", "Kota", "Indore", "Jaipur"])
occupation = st.selectbox("Occupation", options=['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'])


if st.button("Predict Insurance Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }
    
    response = requests.post(API_URL, json=input_data)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Insurance Premium: {result['predicted_insurance_premium']}")
        st.success(f"Class Probabilities: {result['class_probabilities']}")
    else:
        st.error(f"Error in prediction. Status: {response.status_code}, Response: {response.text}")

