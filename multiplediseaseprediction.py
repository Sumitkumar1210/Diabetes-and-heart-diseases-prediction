import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import requests

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Page configuration
st.set_page_config(page_title="Disease Prediction", layout="centered")
st.markdown("<br><br>", unsafe_allow_html=True)

# Light Mode Theme Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f0f8ff, #e6f2ff);
        background-attachment: fixed;
        padding-top: 3rem; /* ✅ Add this padding */
    }
    .block-container {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
    }
    h1, h2, h3, h4 {
        color: #003366;
        text-align: center;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #f0f8ff;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #004080;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #0059b3;
        transition: 0.3s;
    }
    /* Custom style for Ask AI button */
    .custom-ask-ai-button {
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 1.1rem;
    }
    .custom-ask-ai-button:hover {
        background-color: #218838 !important;
        transition: 0.3s;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Ask AI'],
        icons=['activity', 'heart', 'robot'],
        default_index=0,
    )

# Title
st.title("Multiple Disease Prediction System")

# Function to clear input fields safely
def clear_inputs(keys):
    for key in keys:
        if key in st.session_state:
            st.session_state[key] = ''

# --- Diabetes Prediction ---
if selected == 'Diabetes Prediction':
    st.subheader('🔹 Diabetes Prediction')

    diabetes_keys = ['Pregnancies', 'Glucose', 'BloodPressure', 
                     'SkinThickness', 'Insulin', 'BMI', 
                     'DiabetesPedigreeFunction', 'Age']

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key='Pregnancies', placeholder="e.g., 2")
    with col2:
        Glucose = st.text_input('Glucose Level', key='Glucose', placeholder="e.g., 120")
    with col3:
        BloodPressure = st.text_input('Blood Pressure', key='BloodPressure', placeholder="e.g., 70")
    with col1:
        SkinThickness = st.text_input('Skin Thickness', key='SkinThickness', placeholder="e.g., 20")
    with col2:
        Insulin = st.text_input('Insulin Level', key='Insulin', placeholder="e.g., 85")
    with col3:
        BMI = st.text_input('BMI', key='BMI', placeholder="e.g., 28.5")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', key='DiabetesPedigreeFunction', placeholder="e.g., 0.5")
    with col2:
        Age = st.text_input('Age', key='Age', placeholder="e.g., 30")

    col_predict, col_clear = st.columns(2)

    with col_predict:
        if st.button('Predict Diabetes'):
            try:
                input_data = [float(Pregnancies), float(Glucose), float(BloodPressure),
                              float(SkinThickness), float(Insulin), float(BMI),
                              float(DiabetesPedigreeFunction), float(Age)]
                diab_prediction = diabetes_model.predict([input_data])

                if diab_prediction[0] == 1:
                    st.success('🩺 The person is diabetic.')
                else:
                    st.success('✅ The person is not diabetic.')
                st.balloons()
            except ValueError:
                st.warning('⚠️ Please enter valid numbers in all fields.')

    with col_clear:
        st.button('Clear All', on_click=clear_inputs, args=(diabetes_keys,), key='clear_diabetes')

# --- Heart Disease Prediction ---
if selected == 'Heart Disease Prediction':
    st.subheader('🔹 Heart Disease Prediction')

    heart_keys = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                  'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', key='age', placeholder="e.g., 45")
    with col2:
        sex = st.text_input('Sex (1=Male, 0=Female)', key='sex', placeholder="e.g., 1")
    with col3:
        cp = st.text_input('Chest Pain Type', key='cp', placeholder="e.g., 2")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', key='trestbps', placeholder="e.g., 130")
    with col2:
        chol = st.text_input('Serum Cholesterol', key='chol', placeholder="e.g., 250")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar >120mg/dl (1=True, 0=False)', key='fbs', placeholder="e.g., 0")
    with col1:
        restecg = st.text_input('Resting ECG Result', key='restecg', placeholder="e.g., 1")
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved', key='thalach', placeholder="e.g., 150")
    with col3:
        exang = st.text_input('Exercise Induced Angina (1=Yes, 0=No)', key='exang', placeholder="e.g., 0")
    with col1:
        oldpeak = st.text_input('ST Depression', key='oldpeak', placeholder="e.g., 1.2")
    with col2:
        slope = st.text_input('Slope of ST Segment', key='slope', placeholder="e.g., 2")
    with col3:
        ca = st.text_input('Major Vessels Colored', key='ca', placeholder="e.g., 0")
    with col1:
        thal = st.text_input('Thalassemia (0,1,2)', key='thal', placeholder="e.g., 2")

    col_predict, col_clear = st.columns(2)

    with col_predict:
        if st.button('Predict Heart Disease'):
            try:
                input_data = [int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs),
                              int(restecg), int(thalach), int(exang), float(oldpeak),
                              int(slope), int(ca), int(thal)]
                heart_prediction = heart_disease_model.predict([input_data])

                if heart_prediction[0] == 1:
                    st.success('💔 The person has heart disease.')
                else:
                    st.success('❤️ The person does not have heart disease.')
                st.snow()
            except ValueError:
                st.warning('⚠️ Please enter valid numbers in all fields.')

    with col_clear:
        st.button('Clear All', on_click=clear_inputs, args=(heart_keys,), key='clear_heart')

# --- Ask AI Section ---
if selected == 'Ask AI':
    st.subheader("🧠 Ask AI About Health")

    user_question = st.text_input("Enter your health-related question:", key="ask_ai_input_main")

    if st.markdown('<button class="custom-ask-ai-button">Ask AI</button>', unsafe_allow_html=True):
        if user_question.strip():
            with st.spinner("Getting answer from AI..."):
                try:
                    response = requests.post(
                        "http://localhost:5000/ask_ai",  # Flask API endpoint
                        json={"question": user_question}
                    )
                    if response.status_code == 200:
                        ai_reply = response.json().get("AI Response", "No response received.")
                        st.success("AI says:")
                        st.write(ai_reply)
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
        else:
            st.warning("Please enter a question.")


# python -m streamlit run "multiplediseaseprediction.py"
# python askai.py