import streamlit as st
from prediction_helper import predict

# Set page configuration
st.set_page_config(page_title="Health Insurance Predictor", layout="wide")

# Custom CSS for aesthetic styling
st.markdown("""
    <style>
        /* Light purple background */
        .stApp {
            background: #E6E6FA; /* Lavender */
        }

        /* Title */
        .title {
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            color: black;
            margin-bottom: 10px;
        }

        /* Section Headings */
        .subheading {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            color: black;
            margin-top: 15px;
        }

        /* Container styling */
        .stContainer {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Select, input fields, and sliders */
        .stTextInput, .stNumberInput, .stSelectbox, .stSlider {
            background: white !important;
            color: black !important;
            font-family: 'Poppins', sans-serif;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        /* Sliders - Dark Blue */
        .stSlider > div[role="slider"] {
            background: #1E3A8A !important; /* Dark blue */
        }

        /* Predict Button */
        .stButton>button {
            background: #B39DDB !important; /* Soft pastel purple */
            color: black !important;
            font-size: 16px;
            font-family: 'Poppins', sans-serif;
            padding: 10px;
            border-radius: 6px;
            width: 100%;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: #9575CD !important; /* Slightly darker pastel purple */
        }

        /* Prediction Box */
        .prediction-box {
            background: #C5E1A5; /* Light green */
            color: black;
            padding: 12px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 🌿 Title
st.markdown('<p class="title">Health Insurance Predictor</p>', unsafe_allow_html=True)

# 📋 Ask for User's Name
name = st.text_input("Enter your name")

# Define dropdown categories
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High Blood Pressure', 'Diabetes & High BP',
        'Thyroid', 'Heart Disease', 'BP & Heart Disease', 'Diabetes & Thyroid',
        'Diabetes & Heart Disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# 📋 Dashboard Container
with st.container():
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)

    # 📋 User Details Heading
    st.markdown('<p class="subheading">Enter Your Details</p>', unsafe_allow_html=True)

    # 🎚️ Sliders for age & income
    age = st.slider('Age', min_value=18, max_value=100, value=25)
    income_lakhs = st.slider('Income in Lakhs', min_value=0, max_value=200, value=10)

    # 🏷️ Arrange Inputs in Three-Column Layout
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('Gender', categorical_options['Gender'])
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

    with col2:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
        region = st.selectbox('Region', categorical_options['Region'])
        genetical_risk = st.slider('Genetical Risk', min_value=0, max_value=5, value=2)

    with col3:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

    # Close Container Styling
    st.markdown('</div>', unsafe_allow_html=True)

# 📊 Collect user inputs in a dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# 🔮 Prediction Section
st.markdown('<p class="subheading">Prediction</p>', unsafe_allow_html=True)

# Prediction Button
if st.button('Predict Insurance Cost'):
    prediction = predict(input_dict)
    if name:
        st.markdown(f'<p class="prediction-box">{name}\'s Health Insurance Prediction: {prediction} INR</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="prediction-box">Health Insurance Prediction: {prediction} INR</p>', unsafe_allow_html=True)
