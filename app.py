import streamlit as st
import joblib



st.title("California Housing price")
st.divider()
st.write("## California")

st.write("California Housing price")
x = st.text_input("Enter the value of the feature")

st.write(f"The feature value is: {x}")