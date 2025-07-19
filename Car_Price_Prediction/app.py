import streamlit as st
import pandas as pd
import pickle
import datetime

def load_local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


model = pickle.load(open('car.sav', 'rb'))
# Call it
load_local_css("style.css")




# Brand map
brand_map = {
    'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5,
    'Ford': 6, 'Renault': 7, 'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10,
    'Fiat': 11, 'Datsun': 12, 'Jeep': 13, 'Mercedes-Benz': 14, 'Mitsubishi': 15,
    'Audi': 16, 'Volkswagen': 17, 'BMW': 18, 'Nissan': 19, 'Lexus': 20,
    'Jaguar': 21, 'Land': 22, 'MG': 23, 'Volvo': 24, 'Daewoo': 25,
    'Kia': 26, 'Force': 27, 'Ambassador': 28, 'Ashok': 29, 'Isuzu': 30,
    'Opel': 31, 'Peugeot': 32
}

# Streamlit config
#st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

st.markdown("<h1 style='text-align: center; color: darkblue;'>🚗 Car Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input form
st.markdown("### 🔧 Enter Car Details:")
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Car Brand", list(brand_map.keys()))
    seats = st.number_input("Number of Seats", min_value=2, max_value=10, step=1)
    fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
    transmission = st.radio("Transmission", ['Manual', 'Automatic'])

with col2:
    km_driven = st.slider("KM Driven", min_value=0, max_value=300000, value=30000, step=1000)
    engine = st.slider("Engine Size (cc)", min_value=500, max_value=5000, value=1200, step=100)
    max_power = st.slider("Max Power (bhp)", min_value=20, max_value=500, value=100, step=5)
    torque = st.slider("Torque (Nm)", min_value=10, max_value=600, value=150, step=5)
    mileage = st.slider("Mileage (km/l)", min_value=0.0, max_value=40.0, value=15.0, step=0.1)
    year = st.slider("Manufacturing Year", min_value=2000, max_value=datetime.datetime.now().year, value=2018)

# Prediction logic
if st.button("🔍 Predict Price"):
    brand_code = brand_map[brand]
    fuel_code = {'Petrol': 0, 'Diesel': 1, 'Electric': 2, 'Hybrid': 3}[fuel]
    transmission_code = {'Manual': 0, 'Automatic': 1}[transmission]

    input_df = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel_code],
        'transmission': [transmission_code],
        'mileage': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'torque': [torque],
        'seats': [seats],
        'Brand_Code': [brand_code]
    })

    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 **Predicted Selling Price**: ₹ {predicted_price:,.2f}")
    st.balloons()
