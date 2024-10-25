import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler

import warnings
warnings.filterwarnings('ignore')

# Importing Model
model = pickle.load(open('model.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))


st.title('Heart Failure Predicator')
age = st.number_input('Age of the patient (Years)',min_value=40)
anaemia = st.selectbox('If the patient has anaemia',['Yes','No'])
creatinine_phosphokinase = st.number_input('Level of the Creatinine phosphokinase (CPK) enzyme in the blood (mcg/L)',min_value=float(23))
diabetes = st.selectbox('If the patient has diabetes',['Yes','No'])
ejection_fraction = st.number_input('Percentage of blood leaving the heart at each contraction (Ejection_Fraction)',min_value=float(14))
high_blood_pressure = st.selectbox('If a patient has hypertension',['Yes','No'])
platelets = st.number_input('Platelets in the blood (platelets/mL)',min_value=float(25000))
serum_creatinine = st.number_input('Level of creatinine in the blood (mg/dL)',min_value=float(0.5))
serum_sodium = st.number_input('Level of sodium in the blood (mEq/L)',min_value=float(114))
sex = st.selectbox('Gender of the patient',['Male','Female'])
smoking = st.selectbox('If the patient smokes',['Yes','No'])
time = st.number_input('Follow-up period (days)',min_value=4)

if st.button('Predict Heart Health'):
    pass
   
    if anaemia == 'Yes':
        anaemia = 1
    else:
        anaemia = 0

    if diabetes == 'Yes':
        diabetes = 1
    else:
        diabetes = 0

    if sex == 'Male':
        sex = 1
    else:
        sex = 0

    if smoking == 'Yes':
        smoking = 1
    else:
        smoking = 0

    if high_blood_pressure == 'Yes':
        high_blood_pressure = 1
    else:
        high_blood_pressure = 0

    query = np.array([age, anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure, 
                      platelets,serum_creatinine,serum_sodium,sex,smoking,time])   

    query = query.reshape(1,-1)[0]   
     
    st.title('The propability of mortality caused by Heart Failure based on the given clinical records is ' + str(int(model.predict([query])[0])*100) +' %.')



