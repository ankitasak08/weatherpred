import streamlit as st
import numpy as np
import pickle

model = pickle.load(open(r'C:\Users\Pramod  Sakharkar\Desktop\weatherpred\weatherapp.pkl', 'rb'))

def predict(input_features):

    numeric_features = [float(feature) for feature in input_features]
    return model.predict([np.array(numeric_features)])[0]


def main():
    st.set_page_config(page_title="Nagpur`s Weather Prediction", page_icon="🌡️")

    # Improved CSS
    st.markdown("""
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Helvetica', sans-serif; 
                color: #333;
                text-align: center;
                background-color: #f8f8f8;
            }

            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }

            .box {
                background-color: #fff;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                padding: 30px;
                border-radius: 12px;
                max-width: 600px;
                width: 100%;
                text-align: left;
            }

            .box p {
                font-size: 1.2em;
                margin-bottom: 20px;
            }

            form {
                display: flex;
                flex-direction: column;
                margin-top: 20px;
            }

            input {
                width: 100%;
                padding: 12px;
                margin-bottom: 16px;
                font-size: 1em;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            button {
                background: #4CAF50;
                color: #fff;
                padding: 12px 20px;
                font-size: 1.2em;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                transition: background 0.3s ease;
            }

            button:hover {
                background: #45a049;
            }

            .prediction {
                margin-top: 20px;
                font-size: 1.5em;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)

    # Streamlit app content
    st.title("🍊 Nagpur Weather Prediction ! ⛈️ ")
    st.write("Enter the weather parameters to predict the weather condition.")

    # Input fields
    temperature = st.number_input("Temperature (°F)")
    humidity = st.number_input("Humidity (%)")
    pressure = st.number_input("Pressure (hPa)")
    wind_chill = st.number_input("Wind Chill (°F)")
    wind_speed = st.number_input("Wind Speed (m/s)")
    rain = st.number_input("Rainfall (0 for No and 1 for Yes)")

    # Predict button
    if st.button("Predict Weather Condition"):
        input_features = [temperature, humidity, pressure, wind_chill, wind_speed, rain]
        prediction_text = f"The predicted weather condition is: {predict(input_features)}"
        st.write(prediction_text, className="prediction")

if __name__ == "__main__":
    main()

