import streamlit as st
import numpy as np
import joblib

#page config
st.set_page_config(
    page_title="DiaSense - Smart Diabetes Risk Analyzer",
    page_icon=" ",
    layout="centered",
    initial_sidebar_state="expanded",
)

#Custom css styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            front-size: 38px;
            color: #2A7AE2;
            font-wieght: 800;
            margin-botton:5px;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #4B4B4B
            margin-bottom: 30px;
        }

        .sButton>button {
            width: 100%;
            background-color: #2A7AE2
            color: white;
            font_size: 18px;
            padding: 12px;
            border-radius: 10px;
        }

        .stButton>button:hover {
            background-color: #1F5BB5;
            color: white;
        }     

        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #F0F6FF;
            box-shadow: 1px 1px 10px #d1d1d1;
        }

        .footer {
            text-align: center;
            color: #888888
            font-size: 14px;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

#Load Model and Scaler
model=joblib.load("diabetes_model.pkl")
scaler=joblib.load("scaler.pkl")

#App header
st.markdown('<div class="title">🩺  DiaSense</div>', unsafe_allow_html=True)
st.markdown('<div class="Subtitle">Smart Diabetes Risk Analyzer</div>',
           unsafe_allow_html=True)

#Input Section
st.markdown('<div> class="card">', unsafe_allow_html=True)
col1, col2=st.columns(2)
with col1:
    preg=st.number_input("Pregnancies",0,20,step=1)
    bp=st.number_input("Blood Pressure",0,200)
    insulin=st.number_input("Insulin",0,900)
    dpf=st.number_input("Diabetes Pedigree Function",0.0,3.0)

with col2:
    glucose=st.number_input("Glucose Level",0,300)
    skin=st.number_input("Skin Thickness",0,100)
    bmi=st.number_input("BMI",0.0,70.0)
    age=st.number_input("Age",0,120)
st.markdown('</div',unsafe allow html=True)
st.write("")
predict_btn=st.button("Predict Diabetes Risk")
if predict_btn:
    input_data=np.array([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])
    input_data= scaler.transform(input_data)
    pred=model.predict(input_data)[0][1]
    if pred ==1:
        st.error(f"High Risk:the patient is likely diabetic*,\n\n**Probaability**{prob:.2f}")
    else:
        st.success(f"low Risk: patient is not diabetic*.\n\n**Probability**{prob:.2f"}")
        st.write("----")
        st.markdown(
            "<p class='footer'"
        )
