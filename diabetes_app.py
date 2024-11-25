import streamlit as st
import requests
import json

# Define the scoring URI and headers
scoring_uri = 'http://2f882265-4940-4e6c-8e8e-43b3b77c816e.centralindia.azurecontainer.io/score'
headers = {"Content-Type": "application/json"}

# App title
st.title("Diabetes Prediction App")

# Input fields for user data
st.sidebar.header("Input Parameters")
def get_user_input():
    pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, value=0)
    glucose = st.sidebar.number_input("Glucose Level", min_value=0, value=120)
    blood_pressure = st.sidebar.number_input("Blood Pressure", min_value=0, value=80)
    skin_thickness = st.sidebar.number_input("Skin Thickness", min_value=0, value=20)
    insulin = st.sidebar.number_input("Insulin", min_value=0, value=85)
    bmi = st.sidebar.number_input("BMI", min_value=0.0, value=25.0, step=0.1)
    diabetes_pedigree = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5, step=0.01)
    age = st.sidebar.number_input("Age", min_value=0, value=30)
    return [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]

# Get user input
input_data = get_user_input()

# Button to trigger prediction
if st.button("Predict"):
    input_data_json = json.dumps({"data": [input_data]})
    
    # Send a POST request to the deployed model
    response = requests.post(scoring_uri, data=input_data_json, headers=headers)
    
    if response.status_code == 200:
        result = json.loads(response.json())
        prediction = result["result"][0]
        
        # Display the prediction
        if prediction == 1:
            st.error("The model predicts that the patient is likely to have diabetes.")
        else:
            st.success("The model predicts that the patient is unlikely to have diabetes.")
    else:
        st.error(f"Error: {response.text}")
