# import streamlit as st
# import pickle
# from streamlit_option_menu import option_menu

# # Change Name & Logo
# st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# # Hiding Streamlit add-ons
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Adding Background Image
# background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"  # Replace with your image URL

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] {{
# background-image: url({background_image_url});
# background-size: cover;
# background-position: center;
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

# [data-testid="stAppViewContainer"]::before {{
# content: "";
# position: absolute;
# top: 0;
# left: 0;
# width: 100%;
# height: 100%;
# background-color: rgba(0, 0, 0, 0.7);
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Load the saved models
# # models = {
# #     'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
# #     'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
# #     'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
# #     'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
# #     'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
# # }

# models = {
#     'diabetes': pickle.load(open('C:/Users/insom/OneDrive/Desktop/python pros/Project2_files/Medical diagnosis using AI/Models/diabetes_model.sav', 'rb')),
#     'heart_disease': pickle.load(open('C:/Users/insom/OneDrive/Desktop/python pros/Project2_files/Medical diagnosis using AI/Models/heart_disease_model.sav', 'rb')),
#     'parkinsons': pickle.load(open('C:/Users/insom/OneDrive/Desktop/python pros/Project2_files/Medical diagnosis using AI/Models/parkinsons_model.sav', 'rb')),
#     'lung_cancer': pickle.load(open('C:/Users/insom/OneDrive/Desktop/python pros/Project2_files/Medical diagnosis using AI/Models/lungs_disease_model.sav', 'rb')),
#     'thyroid': pickle.load(open('C:/Users/insom/OneDrive/Desktop/python pros/Project2_files/Medical diagnosis using AI/Models/Thyroid_model.sav', 'rb'))
# }

# # Create a dropdown menu for disease prediction
# selected = st.selectbox(
#     'Select a Disease to Predict',
#     ['Diabetes Prediction',
#      'Heart Disease Prediction',
#      'Parkinsons Prediction',
#      'Lung Cancer Prediction',
#      'Hypo-Thyroid Prediction']
# )

# def display_input(label, tooltip, key, type="text"):
#     if type == "text":
#         return st.text_input(label, key=key, help=tooltip)
#     elif type == "number":
#         return st.number_input(label, key=key, help=tooltip, step=1)

# # Diabetes Prediction Page
# if selected == 'Diabetes Prediction':
#     st.title('Diabetes')
#     st.write("Enter the following details to predict diabetes:")

#     Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
#     Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
#     BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
#     SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
#     Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
#     BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
#     DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
#     Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

#     diab_diagnosis = ''
#     if st.button('Diabetes Test Result'):
#         diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
#         diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
#         st.success(diab_diagnosis)

# # Heart Disease Prediction Page
# if selected == 'Heart Disease Prediction':
#     st.title('Heart Disease')
#     st.write("Enter the following details to predict heart disease:")

#     age = display_input('Age', 'Enter age of the person', 'age', 'number')
#     sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
#     cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
#     trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
#     chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
#     fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
#     restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
#     thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
#     exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
#     oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
#     slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
#     ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
#     thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

#     heart_diagnosis = ''
#     if st.button('Heart Disease Test Result'):
#         heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
#         heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
#         st.success(heart_diagnosis)

# # Parkinson's Prediction Page
# if selected == "Parkinsons Prediction":
#     st.title("Parkinson's Disease")
#     st.write("Enter the following details to predict Parkinson's disease:")

#     fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
#     fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
#     flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
#     Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
#     Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
#     RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
#     PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
#     DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
#     Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
#     Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
#     APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
#     APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
#     APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
#     DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
#     NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
#     HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
#     RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
#     DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
#     spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
#     spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
#     D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
#     PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

#     parkinsons_diagnosis = ''
#     if st.button("Parkinson's Test Result"):
#         parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
#         parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
#         st.success(parkinsons_diagnosis)

# # Lung Cancer Prediction Page
# if selected == "Lung Cancer Prediction":
#     st.title("Lung Cancer")
#     st.write("Enter the following details to predict lung cancer:")

#     GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
#     AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
#     SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
#     YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
#     ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
#     PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
#     CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
#     FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
#     ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
#     WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
#     ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
#     COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
#     SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
#     SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
#     CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

#     lungs_diagnosis = ''
#     if st.button("Lung Cancer Test Result"):
#         lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
#         lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
#         st.success(lungs_diagnosis)

# # Hypo-Thyroid Prediction Page
# if selected == "Hypo-Thyroid Prediction":
#     st.title("Hypo-Thyroid")
#     st.write("Enter the following details to predict hypo-thyroid disease:")

#     age = display_input('Age', 'Enter age of the person', 'age', 'number')
#     sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
#     on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
#     tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
#     t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
#     t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
#     tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

#     thyroid_diagnosis = ''
#     if st.button("Thyroid Test Result"):
#         thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
#         thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
#         st.success(thyroid_diagnosis)


import streamlit as st
import pickle
import os  # Used for creating portable file paths

# --- Page Configuration ---
st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="⚕️",
    layout="centered",  # Optional: "wide" or "centered"
    initial_sidebar_state="auto"  # Optional: "auto", "expanded", "collapsed"
)

# --- Styling ---
# Hiding Streamlit default elements (Menu, Footer, Header)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image and Overlay
# Using a publicly available, relevant image URL. Replace if you have a specific one.
background_image_url = "https://images.unsplash.com/photo-1579684385127-1ef15d508118?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8aGVhbHRoY2FyZSxkb2N0b3IsbWVkaWNhbHx8fHx8fDE2NzgwMDMxNTA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Adding a semi-transparent overlay */
[data-testid="stAppViewContainer"] > .main::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.7); /* Light overlay */
    z-index: -1; /* Place overlay behind content */
}}

/* Style adjustments for better readability on background */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0); /* Transparent header background */
}}

.stApp {{
    color: #1E1E1E; /* Darker text for better contrast on light overlay */
}}

h1, h2, h3, h4, h5, h6 {{
    color: #003366; /* Dark blue headings */
}}

.stButton>button {{
    background-color: #0068c9;
    color: white;
}}

.stSuccess {{
    background-color: #D4EDDA;
    color: #155724;
    border-color: #C3E6CB;
    border-radius: 0.25rem;
    padding: 0.75rem 1.25rem;
}}

.stError {{
    background-color: #F8D7DA;
    color: #721C24;
    border-color: #F5C6CB;
    border-radius: 0.25rem;
    padding: 0.75rem 1.25rem;
}}

.stWarning {{
    background-color: #FFF3CD;
    color: #856404;
    border-color: #FFEEBA;
    border-radius: 0.25rem;
    padding: 0.75rem 1.25rem;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# --- Model Loading ---
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the Models sub-directory
models_dir = os.path.join(script_dir, 'Models')

# Function to load a model, handling potential errors


def load_model(filename):
    filepath = os.path.join(models_dir, filename)
    try:
        with open(filepath, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error(
            f"Error: Model file not found at {filepath}. Make sure the 'Models' folder exists in the same directory as 'app.py' and contains the file '{filename}'.")
        return None
    except Exception as e:
        st.error(f"Error loading model file '{filename}': {e}")
        return None


# Load models using relative paths and error handling
# Ensure your model filenames match exactly (including case)
models = {
    'diabetes': load_model('diabetes_model.sav'),
    'heart_disease': load_model('heart_disease_model.sav'),
    'parkinsons': load_model('parkinsons_model.sav'),
    # Make sure this filename is correct
    'lung_cancer': load_model('lungs_disease_model.sav'),
    # Make sure this filename is correct
    'thyroid': load_model('Thyroid_model.sav')
}

# Check if all models loaded successfully
if not all(models.values()):
    st.stop()  # Stop execution if any model failed to load

# --- Sidebar Navigation ---
# Using st.sidebar for navigation keeps the main area cleaner
with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png",
             width=150)  # Placeholder logo
    st.title("Prediction Menu")
    selected = st.selectbox(
        'Select a Disease',
        ['Diabetes',
         'Heart Disease',
         'Parkinsons',
         'Lung Cancer',
         'Hypo-Thyroid'],
        label_visibility="collapsed"  # Hides the explicit label above the selectbox
    )

# --- Input Field Helper Function ---
# Ensures consistent creation of number inputs


def display_input(label, tooltip, key):
    # Use number_input for all numerical fields
    # Set format='%f' to avoid potential scientific notation for large/small numbers
    # Add min_value=0 where applicable (e.g., age, counts, levels)
    # Step can be adjusted based on expected precision (e.g., 0.01 for BMI/functions)
    step_val = 1.0
    min_val = 0.0
    if "Level" in label or "value" in label or "Hz" in label or "%" in label or "BMI" in label or "Function" in label or "Rate" in label or "depression" in label or "DDP" in label or "Shimmer" in label or "APQ" in label or "DDA" in label or "NHR" in label or "HNR" in label or "RPDE" in label or "DFA" in label or "spread" in label or "D2" in label or "PPE" in label:
        step_val = 0.001  # Finer step for continuous values
        min_val = None  # Allow negative values if applicable (e.g., spread)
    if "Age" in label:
        min_val = 0.0
        step_val = 1.0

    return st.number_input(label, key=key, help=tooltip, min_value=min_val, step=step_val, format='%f')

# --- Page Content based on Selection ---


# Diabetes Prediction Page
if selected == 'Diabetes':
    st.title('Diabetes Prediction')
    st.markdown(
        "Enter the following details to predict the likelihood of diabetes.")

    with st.form(key='diabetes_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = display_input(
                'Pregnancies', 'Number of times pregnant', 'Pregnancies')
            BloodPressure = display_input(
                'Blood Pressure (mm Hg)', 'Diastolic blood pressure', 'BloodPressure')
            Insulin = display_input(
                'Insulin Level (mu U/ml)', '2-Hour serum insulin', 'Insulin')
        with col2:
            Glucose = display_input(
                'Glucose Level', 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test', 'Glucose')
            SkinThickness = display_input(
                'Skin Thickness (mm)', 'Triceps skin fold thickness', 'SkinThickness')
            BMI = display_input('BMI (kg/m²)', 'Body mass index', 'BMI')
        with col3:
            Age = display_input('Age (years)', 'Age of the person', 'Age')
            DiabetesPedigreeFunction = display_input(
                'Diabetes Pedigree Fn', 'Diabetes pedigree function value', 'DiabetesPedigreeFunction')

        submitted = st.form_submit_button('Predict Diabetes')

        if submitted:
            # Basic check if fields seem filled (st.number_input defaults to 0 if empty)
            # More robust validation could check ranges if necessary
            input_values = [Pregnancies, Glucose, BloodPressure,
                            SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            # Check if any input failed (though unlikely with number_input default)
            if None in input_values:
                st.warning("Please ensure all fields are filled correctly.")
            else:
                try:
                    # Convert all inputs to float for consistency before prediction
                    input_data_float = [float(x) for x in input_values]
                    diab_prediction = models['diabetes'].predict(
                        [input_data_float])
                    if diab_prediction[0] == 1:
                        st.error('Prediction: The person is likely Diabetic.')
                    else:
                        st.success(
                            'Prediction: The person is likely Not Diabetic.')
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")


# Heart Disease Prediction Page
elif selected == 'Heart Disease':
    st.title('Heart Disease Prediction')
    st.markdown(
        "Enter the following details to predict the likelihood of heart disease.")

    with st.form(key='heart_disease_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            age = display_input('Age (years)', 'Age of the person', 'age')
            trestbps = display_input(
                'Resting BP (mm Hg)', 'Resting blood pressure', 'trestbps')
            fbs = display_input('Fasting BS > 120 mg/dl',
                                '1 = true; 0 = false', 'fbs')
            exang = display_input(
                'Exercise Angina', 'Exercise induced angina (1 = yes; 0 = no)', 'exang')
            ca = display_input(
                'Major vessels (0-3)', 'Number of major vessels colored by fluoroscopy', 'ca')
        with col2:
            sex = display_input('Sex', '1 = male; 0 = female', 'sex')
            chol = display_input('Cholesterol (mg/dl)',
                                 'Serum cholesterol', 'chol')
            restecg = display_input(
                'Resting ECG', 'Results (0, 1, 2)', 'restecg')
            oldpeak = display_input(
                'ST depression', 'ST depression induced by exercise relative to rest', 'oldpeak')
            thal = display_input(
                'Thal', '0 = normal; 1 = fixed defect; 2 = reversible defect', 'thal')
        with col3:
            cp = display_input('Chest Pain Type', 'Value 0-3', 'cp')
            thalach = display_input(
                'Max Heart Rate', 'Maximum heart rate achieved', 'thalach')
            slope = display_input(
                'Slope of ST segment', 'Peak exercise ST segment slope (0, 1, 2)', 'slope')

        submitted = st.form_submit_button('Predict Heart Disease')

        if submitted:
            input_values = [age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak, slope, ca, thal]
            if None in input_values:
                st.warning("Please ensure all fields are filled correctly.")
            else:
                try:
                    input_data_float = [float(x) for x in input_values]
                    heart_prediction = models['heart_disease'].predict(
                        [input_data_float])
                    if heart_prediction[0] == 1:
                        st.error(
                            'Prediction: The person likely has Heart Disease.')
                    else:
                        st.success(
                            'Prediction: The person likely does not have Heart Disease.')
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")


# Parkinson's Prediction Page
elif selected == "Parkinsons":
    st.title("Parkinson's Disease Prediction")
    st.markdown(
        "Enter the following voice measurements to predict Parkinson's disease.")

    with st.form(key='parkinsons_form'):
        st.subheader("MDVP Measurements")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fo = display_input('Avg Vocal Freq (Fo Hz)',
                               'Average vocal fundamental frequency', 'fo')
            Jitter_percent = display_input(
                'Jitter (%)', 'MDVP:Jitter(%)', 'Jitter_percent')
            Shimmer = display_input('Shimmer', 'MDVP:Shimmer', 'Shimmer')
            APQ = display_input('APQ', 'MDVP:APQ', 'APQ')
        with col2:
            fhi = display_input('Max Vocal Freq (Fhi Hz)',
                                'Maximum vocal fundamental frequency', 'fhi')
            Jitter_Abs = display_input(
                'Jitter (Abs)', 'MDVP:Jitter(Abs)', 'Jitter_Abs')
            Shimmer_dB = display_input(
                'Shimmer (dB)', 'MDVP:Shimmer(dB)', 'Shimmer_dB')
            DDA = display_input('Shimmer DDA', 'Shimmer:DDA', 'DDA')
        with col3:
            flo = display_input('Min Vocal Freq (Flo Hz)',
                                'Minimum vocal fundamental frequency', 'flo')
            RAP = display_input('RAP', 'MDVP:RAP', 'RAP')
            APQ3 = display_input('APQ3', 'Shimmer:APQ3', 'APQ3')
            NHR = display_input('NHR', 'Noise-to-Harmonics Ratio', 'NHR')
        with col4:
            PPQ = display_input('PPQ', 'MDVP:PPQ', 'PPQ')
            DDP = display_input('DDP', 'Jitter:DDP', 'DDP')
            APQ5 = display_input('APQ5', 'Shimmer:APQ5', 'APQ5')
            HNR = display_input('HNR', 'Harmonics-to-Noise Ratio', 'HNR')

        st.subheader("Nonlinear/Complexity Measures")
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            RPDE = display_input(
                'RPDE', 'Recurrence Period Density Entropy', 'RPDE')
            spread1 = display_input(
                'spread1', 'Nonlinear measure of fundamental frequency variation', 'spread1')
        with col6:
            DFA = display_input('DFA', 'Detrended Fluctuation Analysis', 'DFA')
            spread2 = display_input(
                'spread2', 'Nonlinear measure of fundamental frequency variation', 'spread2')
        with col7:
            D2 = display_input('D2', 'Correlation Dimension', 'D2')
        with col8:
            PPE = display_input('PPE', 'Pitch Period Entropy', 'PPE')

        submitted = st.form_submit_button("Predict Parkinson's")

        if submitted:
            input_values = [
                fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer,
                Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1,
                spread2, D2, PPE
            ]
            if None in input_values:
                st.warning("Please ensure all fields are filled correctly.")
            else:
                try:
                    input_data_float = [float(x) for x in input_values]
                    parkinsons_prediction = models['parkinsons'].predict(
                        [input_data_float])
                    if parkinsons_prediction[0] == 1:
                        st.error(
                            "Prediction: The person likely has Parkinson's disease.")
                    else:
                        st.success(
                            "Prediction: The person likely does not have Parkinson's disease.")
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")


# Lung Cancer Prediction Page
elif selected == "Lung Cancer":
    st.title("Lung Cancer Prediction")
    st.markdown(
        "Enter the following details to predict the likelihood of lung cancer.")

    with st.form(key='lung_cancer_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            GENDER = display_input('Gender', '1 = Male; 0 = Female', 'GENDER')
            YELLOW_FINGERS = display_input(
                'Yellow Fingers', '1 = Yes; 0 = No', 'YELLOW_FINGERS')
            CHRONIC_DISEASE = display_input(
                'Chronic Disease', '1 = Yes; 0 = No', 'CHRONIC_DISEASE')
            WHEEZING = display_input('Wheezing', '1 = Yes; 0 = No', 'WHEEZING')
            SHORTNESS_OF_BREATH = display_input(
                'Shortness Of Breath', '1 = Yes; 0 = No', 'SHORTNESS_OF_BREATH')
        with col2:
            AGE = display_input('Age (years)', 'Age of the person', 'AGE')
            ANXIETY = display_input('Anxiety', '1 = Yes; 0 = No', 'ANXIETY')
            FATIGUE = display_input('Fatigue', '1 = Yes; 0 = No', 'FATIGUE')
            ALCOHOL_CONSUMING = display_input(
                'Alcohol Consuming', '1 = Yes; 0 = No', 'ALCOHOL_CONSUMING')
            SWALLOWING_DIFFICULTY = display_input(
                'Swallowing Difficulty', '1 = Yes; 0 = No', 'SWALLOWING_DIFFICULTY')
        with col3:
            SMOKING = display_input('Smoking', '1 = Yes; 0 = No', 'SMOKING')
            PEER_PRESSURE = display_input(
                'Peer Pressure', '1 = Yes; 0 = No', 'PEER_PRESSURE')
            ALLERGY = display_input('Allergy', '1 = Yes; 0 = No', 'ALLERGY')
            COUGHING = display_input('Coughing', '1 = Yes; 0 = No', 'COUGHING')
            CHEST_PAIN = display_input(
                'Chest Pain', '1 = Yes; 0 = No', 'CHEST_PAIN')

        submitted = st.form_submit_button("Predict Lung Cancer")

        if submitted:
            input_values = [
                GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
                CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING,
                COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN
            ]
            # Check for binary values (0 or 1) might be useful here if model expects strict 0/1
            valid_binary = all(val in [0.0, 1.0] for i, val in enumerate(
                input_values) if i != 1)  # Exclude AGE
            if None in input_values:
                st.warning("Please ensure all fields are filled correctly.")
            # elif not valid_binary: # Optional stricter check
            #    st.warning("Please ensure binary inputs (Yes/No fields) are either 0 or 1.")
            else:
                try:
                    input_data_float = [float(x) for x in input_values]
                    lungs_prediction = models['lung_cancer'].predict(
                        [input_data_float])
                    if lungs_prediction[0] == 1:
                        st.error(
                            "Prediction: The person likely has Lung Cancer.")
                    else:
                        st.success(
                            "Prediction: The person likely does not have Lung Cancer.")
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")


# Hypo-Thyroid Prediction Page
elif selected == "Hypo-Thyroid":
    st.title("Hypo-Thyroid Prediction")
    st.markdown("Enter the following details to predict hypo-thyroidism.")

    with st.form(key='thyroid_form'):
        col1, col2 = st.columns(2)
        with col1:
            age = display_input('Age (years)', 'Age of the person', 'age')
            on_thyroxine = display_input(
                'On Thyroxine', '1 = Yes; 0 = No', 'on_thyroxine')
            t3_measured = display_input(
                'T3 Measured', '1 = Yes; 0 = No', 't3_measured')
            tt4 = display_input('TT4 Level', 'Total Thyroxine level', 'tt4')

        with col2:
            sex = display_input('Sex', '1 = Male; 0 = Female', 'sex')
            tsh = display_input(
                'TSH Level', 'Thyroid-Stimulating Hormone level', 'tsh')
            t3 = display_input('T3 Level', 'Triiodothyronine level', 't3')

        submitted = st.form_submit_button("Predict Hypo-Thyroid")

        if submitted:
            input_values = [age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]
            # TSH, T3, TT4 might be 0 if not measured - check if model handles this or if validation needed
            if None in input_values:
                st.warning("Please ensure all fields are filled correctly.")
            else:
                try:
                    input_data_float = [float(x) for x in input_values]
                    thyroid_prediction = models['thyroid'].predict(
                        [input_data_float])
                    if thyroid_prediction[0] == 1:
                        st.error(
                            "Prediction: The person likely has Hypo-Thyroid disease.")
                    else:
                        st.success(
                            "Prediction: The person likely does not have Hypo-Thyroid disease.")
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")


# --- Footer ---
st.markdown("---")
st.markdown("Disclaimer: This prediction is based on machine learning models and is not a substitute for professional medical advice. Consult a doctor for accurate diagnosis.")
