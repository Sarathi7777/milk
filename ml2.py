import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('data.pkl','rb'))

def predict(pH,Temprature,Taste,Odor,Fat,Turbidity,Colour):
    input=np.array([[pH,Temprature,Taste,Odor,Fat,Turbidity,Colour]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0],2) 
    return float(pred)
def main():
    st.title("Prediction")
    html_temp="""
    <div style="background-color:#00A19B ;padding:10px;">
    <h2 style="color:black;text-align:center;">Milk Quality Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    pH = st.text_input("pH")
    Temprature = st.text_input("Temprature")
    Taste = st.text_input("Taste")
    Odor = st.text_input("Odor")
    Fat = st.text_input("Fat")
    Turbidity = st.text_input("Turbidity")
    Colour = st.text_input("Colour")
    safe_html="""
    <div style="background-color:#00A19B;padding:10px">
    <h2 style="color:white;text-align:center;">Your milk is good</h2>
    </div>
    """
    danger_html="""
    <div style="background-color:#00A19B;padding:10px">
    <h2 style="color:black;text-align:center;">Your milk is bad</h2>
    </div>
    """
    if st.button("Predict"):
        output=predict(pH,Temprature,Taste,Odor,Fat,Turbidity,Colour)
        if output>0.5:
            st.markdown(safe_html,unsafe_allow_html=True)
        else:
            st.markdown(danger_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()
