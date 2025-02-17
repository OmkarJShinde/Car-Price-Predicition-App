import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("CarProject.pkl", "rb") as file:
    model = pickle.load(file)

df = pd.read_csv("cleaning_car.csv")

companies = sorted(df["company"].unique())
fuel_types = sorted(df["fuel_type"].unique())
years = sorted(df["year"].unique(), reverse=True)

def get_models(company):
    return df[df["company"] == company]["name"].unique()

# Streamlit UI
 
st.title("Car Price Prediction App 🚗")

st.sidebar.header("Enter Car Details")

# Company Selection
selected_company = st.sidebar.selectbox("Select Company", companies)

# Model Selection (depends on selected company)
models = get_models(selected_company)
selected_model = st.sidebar.selectbox("Select Model", models)

# Year Selection
selected_year = st.sidebar.selectbox("Select Year", years)

# Kilometers Driven Input
kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, step=1000)

# Fuel Type Selection
selected_fuel_type = st.sidebar.selectbox("Select Fuel Type", fuel_types)

# Predict button
if st.sidebar.button("Predict Price"):
    input_data = pd.DataFrame(
        [[selected_company, selected_model, selected_year, kms_driven, selected_fuel_type]],
        columns=["company", "name", "year", "kms_driven", "fuel_type"]
    )

    # Predict price
    prediction = model.predict(input_data)[0,0]

    # Display result
    st.success(f"Predicted Price: ₹ {round(prediction, 2)}")

