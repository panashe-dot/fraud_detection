import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import joblib  # For model persistence



# Model loading and prediction function (assuming the model is already saved)
def load_model_and_predict(data):
  model='model.joblib'
  model=joblib.load(model)
  predictions = model.predict(data)
  return predictions

categories = ['barsandrestaurants', 'contents', 'fashion', 'food', 'health',
           'home', 'hotelservices', 'hyper', 'leisure', 'otherservices',
           'sportsandtoys', 'tech', 'transportation', 'travel']
# Input form
st.title("Fraud Detection App")
st.write("Enter transaction details to check for:")
step = st.number_input("Step",min_value=0)
age = st.number_input("Age", min_value=0)
gender = st.radio("Gender", ("Male", "Female"))
merchant = st.selectbox("Merchant", (30,18))
category = st.selectbox("Category",('barsandrestaurants','contents','fashion','food','health','home','hotelservices','hyper','leisure','otherservices','sportsandtoys','tech','transportation','travel'))
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
    "step":float(step), 
    "age":float(age),
    "gender":float(gender),
    "merchant":float(merchant),
    "category":float(1),
    "amount":float(amount)
    }
   st.write(step,age,gender,merchant,category,amount)
