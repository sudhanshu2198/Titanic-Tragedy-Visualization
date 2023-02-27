import streamlit as st 
import pandas as pd
import numpy as np
import os

st.error("Prediction Survices will be functional in near future")
st.title("Survival Prediction")
with st.form('user_inputs'):
    Embarked=st.selectbox("Point of Departure",('Southampton', 'Cherbourg', 'Queenstown'))
    Class=st.selectbox("Social Status",('Upper', 'Lower', 'Middle'))
    Sex=st.selectbox("Gender of passenger",('male', 'female'))
    No_of_siblings=st.number_input("No of siblings on ship",min_value=0,max_value=4,value=2,step=1)
    No_of_parents=st.number_input("No of parents on ship(include paternal and maternal )",min_value=0,max_value=4,value=2,step=1)
    Fare=st.number_input("Ticket Price",min_value=0.0,max_value=512.0,value=100.0,step=1.0)
    Age=st.number_input("Age of passenger",min_value=0.5,max_value=80.0,value=20.0,step=0.5)
    st.form_submit_button()