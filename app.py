import streamlit as st
import joblib
from streamlit_folium import st_folium
import folium
import numpy as np
import pandas as pd
from feature_engineering import FeatureEngineer

model = joblib.load('xgb_model.pkl')

st.title("California Housing price")

st.markdown("""
Predict California housing prices using an **XGBoost Regression** model.

### How to use
- 📍 Enter the location details in the sidebar.
- 🏠 Provide the housing and neighborhood information.
- 🔮 Click **Predict** to estimate the house price.

""")

with st.sidebar:
    st.info(
    "This demonstration uses the California Housing dataset. "
    "Some inputs (such as Population and Households) describe "
    "the surrounding census block rather than an individual property."
    )

    st.header("📍 Location")
    col1, col2 = st.columns(2)
    with col1:       
        longitude = st.number_input(
            "Longitude",
            value=-122.23,
            help="Longitude of the location."
        )
    with col2:            
        latitude = st.number_input(
            "Latitude",
            value=37.88,
            help="Latitude of the location."
        )

    ocean_proximity = st.selectbox(
            "Ocean Proximity",
            [
                "<1H OCEAN",
                "INLAND",
                "NEAR OCEAN",
                "NEAR BAY",
                "ISLAND",
            ]
        )

    st.header("🏠 Housing")
    
    col1, col2 = st.columns(2)
    with col1:
        total_rooms = st.number_input(
            "Total Rooms",
            min_value=1.0,
            value=2635.76,
            help="Estimated total number of rooms in the census block."
        )
    with col2:
        total_bedrooms = st.number_input(
            "Total Bedrooms",
            min_value=1.0,
            value=537.87,
            help="Estimated total number of bedrooms in the census block."
        )

    housing_median_age = st.number_input(
            "House Age",
            min_value=1.0,
            value=28.64,
            help="Approximate median age of houses in the area."
        )

    st.header("👥 Neighborhood")    
    col1, col2 = st.columns(2)
    with col1:
        population = st.number_input(
            "Population",
            min_value=1.0,
            value=1425.48,
            help="Estimated total number of people living in the census block."
        )
    with col2:
        households = st.number_input(
            "Households",
            min_value=1.0,
            value=499.54,
            help="Estimated number of households in the census block."
        )

    median_income = st.number_input(
        "Median Income",
        min_value=0.0,
        value=3.87,
        help="Median household income (measured in tens of thousands of US dollars)."
    )

    st.divider()
    X = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean_proximity]
    })

    predictbutton = st.button("Predict!")

    if predictbutton:
        pass
        prediction = model.predict(X)[0]
        st.success(
        f"🏠 Predicted House Price: ${prediction:,.2f}"
        )
    


m = folium.Map(location=[latitude,longitude],zoom_start=9,
    scrollWheelZoom=False)


folium.Marker(
    [latitude,longitude],
    popup=f"""
    <b>Selected Location</b><br>
    Latitude: {latitude}<br>
    Longitude: {longitude}
    """,
    tooltip="Selected Property",
    icon=folium.Icon(color="red",icon="home",prefix="fa")
).add_to(m)

st_folium(m,width=700,height=500)