import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import joblib  # For model persistence

# Model loading and prediction function (assuming the model is already saved)
def load_model_and_predict(data):
    model = joblib.load('model.joblib')  # Adjust path if needed
    predictions = model.predict(data)
    return predictions

# Load the model if it exists
try:
    model = load_model_and_predict(pd.DataFrame([]))
except (FileNotFoundError, RuntimeError):
    st.error("Fraud detection model not found. Please train and save a model first.")
    st.stop()
categories = ['barsandrestaurants', 'contents', 'fashion', 'food', 'health',
           'home', 'hotelservices', 'hyper', 'leisure', 'otherservices',
           'sportsandtoys', 'tech', 'transportation', 'travel']
# Input form
st.title("Fraud Detection App")
st.write("Enter transaction details to check for:")
step = st.number_input("Step", min_value=0,max_value=179)
age = st.number_input("Age", min_value=0,max_value=100)
gender = st.radio("Gender", ("Male", "Female"))
merchant = st.selectbox("Merchant", ("30", "18"))
category = st.selectbox("Category",(categories))
amount = st.number_input("Amount", min_value=0.0)

# Prediction button and result display
if st.button("Predict Fraud"):
    if gender=="Male":
        gender=2
    else:
        gender=1
    if categories=='barsandrestaurants':
        category=0
    elif category=='contents':
        category==1
    elif category=='fashion':
        category==2
    elif category=='food':
        category==3
    elif category=='health':
        category==4
    elif category=='home':
         category==5
    elif category=='hotelservices':
         category==6
    elif category=='hyper':
         category==7               
    elif category=='leisure':
         category==8
    elif category=='otherservices':
        category==9                 
    elif category=='sportsandtoys':
        category==10
    elif category=='tech':
        category==11       
    elif category=='transportation':
        category==12                
    elif category=='travel':
        category==13             
    # Prepare input data (adjust based on your model's requirements)
    data = {
    "step":step,  # Replace with your actual data
    "age":age,
    "gender":gender,
    "merchant":merchant,
    "category":category,
    "amount":amount
    }
    data_df = pd.DataFrame([data])


    # Make prediction
    prediction = load_model_and_predict(data)[0]

    # Format and display result
    if prediction >= 0.5:
        st.success("**Potential Fraud Detected (Predicted: 1)**")
    else:
        st.info("**Low Fraud Risk (Predicted: 0)**")
st.set_page_config(layout="wide")
st.markdown("""
<style>
body { background-color: #f0f0f0; }
.reportview-container { background-color: #fff; }
.main { padding: 1rem; }
h1, h2, h3 { color: #333; }
.stInput { padding: 0.5rem 1rem; margin-bottom: 1rem; }
button { background-color: #4CAF50; color: white; padding: 1rem 2rem; border: none; cursor: pointer; border-radius: 5px; }
button:hover { background-color: #3e8e41; }
.success { color: green; }
.info { color: blue; }
</style>
""", unsafe_allow_html=True)





