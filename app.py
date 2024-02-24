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



def map_category_to_integer(category):
    category_map = {
        "barsandrestaurants": 0,
        "contents": 1,
        "fashion": 2,
        "food": 3,
        "health": 4,
        "home": 5,
        "hotelservices": 6,
        "hyper": 7,
        "leisure": 8,
        "otherservices": 9,
        "sportsandtoys": 10,
        "tech": 11,
        "transportation": 12,
        "travel": 13,
    }

    return category_map.get(category)


# Prediction button and result display
if st.button("Predict Fraud"):
    if gender=="Male":
        gender=2
    else:
        gender=1            
    # Prepare input data (adjust based on your model's requirements)
    data = {
    "step":float(step), 
    "age":float(age),
    "gender":float(gender),
    "merchant":float(merchant),
    "category":float(map_category_to_integer(category)),
    "amount":float(amount)
    }
    data_df = pd.DataFrame([data])
    prediction = load_model_and_predict(data_df)[0]
    if prediction >= 0.5:
        st.success("**Fraud Detected**")
    else:
        st.info("**No Fraud Detected**")

