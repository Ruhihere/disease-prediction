# import os
# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu
# import pandas as pd

# st.set_page_config(page_title="Prediction Of Disease Outbreak",
#                     layout="wide",
#                     page_icon='doctor')

# # Load models
# diabetes_model = pickle.load(open(r"C:\Users\ruhip\OneDrive\Desktop\disease_outbreak\training_models\diabetes_model.sav", 'rb'))
# heart_disease_model = pickle.load(open(r"C:\Users\ruhip\OneDrive\Desktop\disease_outbreak\training_models\heart_disease_model.sav", 'rb'))
# parkinson_model = pickle.load(open(r"C:\Users\ruhip\OneDrive\Desktop\disease_outbreak\training_models\parkinsons_model.sav", 'rb'))

# with st.sidebar:
#     selected = option_menu('Prediction of Disease Outbreak System',
#                            ['Diabetes Prediction', 'Heart Disease prediction', 'Parkinsons Prediction'],
#                            menu_icon='hospital-fill',
#                            icons=['activity', 'heart', 'person'],
#                            default_index=0)

# if selected == 'Diabetes Prediction':
#     st.title('Diabetes Prediction using ML')
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         Pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=0)
#     with col2:
#         Glucose = st.number_input('Glucose level', min_value=0, value=0)
#     with col3:
#         BloodPressure = st.number_input('BloodPressure value', min_value=0, value=0)
#     with col1:
#         Skinthickness = st.number_input('Skinthickness value', min_value=0, value=0)
#     with col2:
#         Insulin = st.number_input('Insulin level', min_value=0, value=0)
#     with col3:
#         BMI = st.number_input('BMI value', min_value=0.0, value=0.0)
#     with col1:
#         DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, value=0.0)
#     with col2:
#         Age = st.number_input('Age of the person', min_value=0, value=0)

#     diab_diagnosis = ''
#     if st.button('Diabetes Test result'):
#         try:
#             user_input = [Pregnancies, Glucose, BloodPressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
#             user_input_df = pd.DataFrame([user_input], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
#             diab_prediction = diabetes_model.predict(user_input_df)

#             if diab_prediction[0] == 1:
#                 diab_diagnosis = 'The person is diabetic'
#             else:
#                 diab_diagnosis = 'The person is not diabetic'

#             st.success(diab_diagnosis)

#         except Exception as e:
#             st.error(f"An error occurred: {e}")  # More general error message

# if selected == 'Heart Disease prediction':
#     st.title('Heart Disease Prediction using ML')
    
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         age = st.number_input("Age", min_value=0, value=0)
#     with col2:
#         sex = st.number_input('Sex (0 for female, 1 for male)', min_value=0, max_value=1, value=0)
#     with col3:
#         cp = st.number_input('Chest pain types (0-3)', min_value=0, max_value=3, value=0)
#     with col1:
#         trestbps = st.number_input("Resting Blood Pressure", min_value=0, value=0)
#     with col2:
#         chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, value=0)
#     with col3:
#         fbs = st.number_input('Fasting Blood Sugar >120 mg/dl (0 or 1)', min_value=0, max_value=1, value=0)
#     with col1:
#         restecg = st.number_input('Resting Electrocardiographic results (0-2)', min_value=0, max_value=2, value=0)
#     with col2:
#         thalach = st.number_input('Maximum Heart Rate achieved', min_value=0, value=0)
#     with col3:
#         exang = st.number_input('Exercise Induced Angina (0 or 1)', min_value=0, max_value=1, value=0)
#     with col1:
#         oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, value=0.0)
#     with col2:
#         slope = st.number_input('Slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2, value=0)
#     with col3:
#         ca = st.number_input('Major vessels colored by fluoroscopy (0-3)', min_value=0, max_value=3, value=0)
#     with col1:
#         thal = st.number_input('Thal: normal (0), fixed defect (1), reversible defect (2)', min_value=0, max_value=3, value=0)

#     heart_diagnosis = ''

#     if st.button('Heart Disease Test Result'):
#         try:
#             user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
#             user_input = [float(x) for x in user_input]  # Ensure all inputs are floats
#             user_input_df = pd.DataFrame([user_input], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

#             heart_prediction = heart_disease_model.predict(user_input_df)

#             if heart_prediction[0] == 1:
#                 heart_diagnosis = 'The person has heart disease'
#             else:
#                 heart_diagnosis = 'The person does not have heart disease'

#             st.success(heart_diagnosis)

#         except Exception as e:
#             st.error(f"An error occurred: {e}")


# # if selected == 'Heart Disease Prediction':
# #     st.title('Heart Disease Prediction using ML')
# #     col1, col2, col3 = st.columns(3)

# #     # ... (Heart disease input fields - use st.number_input)
# #     with col1:
# #         age = st.number_input("Age", min_value=0, value=0)
# #     with col2:
# #         sex = st.number_input('Sex (0 for female, 1 for male)', min_value=0, max_value=1, value=0)  # Make sure to handle this properly.
# #     with col3:
# #         cp = st.number_input('Chest pain types (0-3)', min_value=0, max_value=3, value=0)  # Make sure to handle this properly.
# #     with col1:
# #         trestbps = st.number_input("Resting Blood Pressure", min_value=0, value=0)
# #     with col2:
# #         chol = st.number_input('Serum Cholestoral in mg/d1', min_value=0, value=0)
# #     with col3:
# #         fbs = st.number_input('Fasting Blood Sugar >120 mg/dl (0 or 1)', min_value=0, max_value=1, value=0)
# #     with col1:
# #         restecg = st.number_input('Resting Electrocardiographic results (0-2)', min_value=0, max_value=2, value=0)
# #     with col2:
# #         thalach = st.number_input('Maximum Heart Rate achieved', min_value=0, value=0)
# #     with col3:
# #         exang = st.number_input('Exercise Induced Angina (0 or 1)', min_value=0, max_value=1, value=0)
# #     with col1:
# #         oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, value=0.0)
# #     with col2:
# #         slope = st.number_input('slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2, value=0)
# #     with col3:
# #         ca = st.number_input('Major vessels colored by flourosopy (0-3)', min_value=0, max_value=3, value=0)
# #     with col1:
# #         thal = st.number_input('thal: normal; 1 fixed defect; 2 reversable defect (0-3)', min_value=0, max_value=3, value=0)


# #     heart_diagnosis = ''
# #     # if st.button('Heart Disease Test Result'):
# #     #     try:
# #     #         user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
# #     #         user_input_df = pd.DataFrame([user_input], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']) # Add column names
# #     #         heart_prediction = heart_disease_model.predict(user_input_df)
# #     #         if heart_prediction[0] == 1:
# #     #             heart_diagnosis = 'The person is having heart disease'
# #     #         else:
# #     #             heart_diagnosis = 'The person does not have any heart disease'
# #     #         st.success(heart_diagnosis)
# #     #     except Exception as e:
# #     #         st.error(f"An error occurred: {e}")
# #     # ... (Your input fields using st.number_input)

# #     if st.button('Heart Disease Test Result'):
# #         try:
# #             user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]  # Define user_input
# #             user_input = [float(x) for x in user_input]  # Convert to floats ONCE
# #             user_input_df = pd.DataFrame([user_input], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
# #             st.write(user_input_df)  # Debugging: Check the DataFrame
# #             heart_prediction = heart_disease_model.predict(user_input_df)  # Use the DataFrame
# #             # ... (Rest of your code to display results)

# #         except Exception as e:
# #             st.error(f"An error occurred: {e}")


# if selected == "Parkinsons Prediction":
#     st.title("Parkinson's Disease Prediction using ML")

#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         fo = st.text_input('MDVP: Fo(Hz)')
#     with col2:
#         fhi = st.text_input('MDVP: Fhi (Hz)')
#     with col3:
#         flo = st.text_input('MDVP: Flo(Hz)')
#     with col4:
#         Jitter_percent = st.text_input('MDVP: Jitter(%)')
#     with col5:
#         Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
#     with col1:
#         RAP = st.text_input('MDVP: RAP')
#     with col2:
#         PPQ = st.text_input('MDVP: PPQ')
#     with col3:
#         DDP = st.text_input('Jitter: DDP')
#     with col4:
#         Shimmer = st.text_input('MDVP: Shimmer')
#     with col5:
#         Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
#     with col1:
#         APQ3 = st.text_input('Shimmer: APQ3')
#     with col2:
#         APQ5 = st.text_input("Shimmer: APQ5")
#     with col3:
#         APQ = st.text_input('MDVP: APQ')
#     with col4:
#         DDA = st.text_input('Shimmer: DDA')
#     with col5:
#         NHR = st.text_input('NHR')
#     with col1:
#         HNR = st.text_input('HNR')
#     with col2:
#         RPDE = st.text_input('RPDE')
#     with col3:
#         DFA = st.text_input('DFA')
#     with col4:
#         spread1 = st.text_input('spread1')
#     with col5:
#         spread2 = st.text_input('spread2')
#     with col1:
#         D2 = st.text_input('D2')
#     with col2:
#         PPE = st.text_input('PPE')

#     # Code for Prediction
#     parkinsons_diagnosis = ""

#     # Creating a button for Prediction
#     if st.button("Parkinson's Test Result"):
#         try:
#             #  Correctly defining user_input as a list
#             user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
#                           RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
#                           APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

#             # Converting all inputs to float
#             user_input = [float(x) for x in user_input]

#             #  Making prediction
#             parkinsons_prediction = parkinson_model.predict([user_input])

#             # Displaying the result
#             if parkinsons_prediction[0] == 1:
#                 parkinsons_diagnosis = "The person has Parkinson's disease"
#             else:
#                 parkinsons_diagnosis = "The person does not have Parkinson's disease"

#             st.success(parkinsons_diagnosis)

#         except Exception as e:
#             st.error(f"An error occurred: {e}")