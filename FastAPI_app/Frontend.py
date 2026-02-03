import streamlit as st
import requests

st.title("Salary Prediction App")
st.write("Enter your years of experience to predict your salary:")

# Streamlit number input for user experience
experience = st.number_input("Years of Experience", min_value=0.0, max_value=45.0, value=1.0, step=0.1)

if st.button("Predict Salary"):
    # Define the API endpoint (adjust host/port if running elsewhere)
    api_url = "http://localhost:8000/predict"
    payload = {
        "experience": experience
    }

    with st.spinner("Predicting..."):
        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                result = response.json()
                predicted_salary = result.get("predicted_salary", None)
                if predicted_salary is not None:
                    st.success(f"Predicted Salary: ₹{predicted_salary:,.2f}")
                else:
                    st.error("Prediction unavailable. Please try again.")
            else:
                st.error(f"Error from API: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to API: {e}")