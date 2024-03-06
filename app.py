import streamlit as st
import pickle

# Load the pre-trained model
model_loaded = pickle.load(open('model_saved.pkl', 'rb'))

# Define the function for making crop recommendations
def recommend_crop(features):
    test = model_loaded.predict([features])
    return test[0]

# Define the Streamlit app
def main():
    st.title('Crop Recommendation System')
    st.write('Enter the following details to get crop recommendation.')

    # Collect user input for features
    features = []
    features.append(st.number_input('Temperature (°C)', min_value=0.0, max_value=100.0, step=0.1))
    features.append(st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, step=0.1))
    features.append(st.number_input('Rainfall (mm)', min_value=0.0, max_value=1000.0, step=0.1))
    features.append(st.number_input('PH Level', min_value=0.0, max_value=14.0, step=0.1))
    features.append(st.number_input('Nitrogen (ppm)', min_value=0.0, max_value=1000.0, step=0.1))
    features.append(st.number_input('Phosphorus (ppm)', min_value=0.0, max_value=1000.0, step=0.1))
    features.append(st.number_input('Potassium (ppm)', min_value=0.0, max_value=1000.0, step=0.1))

    # Make crop recommendation on button click
    if st.button('Get Recommendation'):
        recommendation = recommend_crop(features)
        st.write('Recommended Crop:', recommendation)

if __name__ == '__main__':
    main()
