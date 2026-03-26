import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 Student Dropout Prediction Dashboard")
st.markdown("""
This dashboard uses an XGBoost machine learning model to predict whether a student is likely to dropout based on their academic and demographic background.
Adjust the parameters below to see how different factors affect the prediction.
""")

@st.cache_resource
def load_model():
    try:
        model = joblib.load('xgb_model.joblib')
        return model
    except FileNotFoundError:
        st.error("Error: 'xgb_model.joblib' not found in the same directory.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is not None:
    st.header("Input Student Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Demographics & Base Info")
        age = st.number_input("Age at enrollment", min_value=15, max_value=100, value=20, step=1)
        gender_male = st.selectbox("Gender", ["Female", "Male"]) == "Male"
        marital_single = st.selectbox("Marital Status", ["Married/Other", "Single"]) == "Single"
        
        st.markdown("---")
        st.subheader("Previous Qualifications")
        admission_grade = st.number_input("Admission grade", min_value=0.0, max_value=200.0, value=120.0, step=0.5)
        prev_qual_grade = st.number_input("Previous qualification grade", min_value=0.0, max_value=200.0, value=130.0, step=0.5)
        
        prev_qual_basic = st.checkbox("Prev qualification: Basic education 3rd cycle")
        prev_qual_secondary = st.checkbox("Prev qualification: Secondary education", value=True)
        app_mode_over23 = st.checkbox("Application mode: Over 23 years old")

    with col2:
        st.subheader("Academic Info (1st Semester)")
        cu_1st_enrolled = st.number_input("1st Sem - Enrolled Units", min_value=0, max_value=30, value=6, step=1)
        cu_1st_approved = st.number_input("1st Sem - Approved Units", min_value=0, max_value=30, value=5, step=1)
        cu_1st_grade = st.number_input("1st Sem - Grade", min_value=0.0, max_value=20.0, value=12.0, step=0.5)
        
        st.markdown("---")
        st.subheader("Academic Info (2nd Semester)")
        cu_2nd_enrolled = st.number_input("2nd Sem - Enrolled Units", min_value=0, max_value=30, value=6, step=1)
        cu_2nd_approved = st.number_input("2nd Sem - Approved Units", min_value=0, max_value=30, value=5, step=1)
        cu_2nd_grade = st.number_input("2nd Sem - Grade", min_value=0.0, max_value=20.0, value=12.0, step=0.5)

    with col3:
        st.subheader("Course Details")
        st.markdown("Check if enrolled in one of these courses:")
        course_inf_eng = st.checkbox("Informatics Engineering")
        course_management_eve = st.checkbox("Management (evening)")
        course_nursing = st.checkbox("Nursing")
        course_social_service = st.checkbox("Social Service")

        st.markdown("---")
        st.subheader("Financial & Social Support")
        scholarship = st.checkbox("Scholarship holder", value=False)
        displaced = st.checkbox("Displaced person", value=False)
        debtor = st.checkbox("Debtor", value=False)
        tuition_up_to_date = st.checkbox("Tuition fees up to date", value=True)
        
        st.markdown("---")
        st.write("")
        st.write("")
        predict_btn = st.button("🔮 Predict Dropout Status", type="primary", use_container_width=True)

    if predict_btn:
        features = {
            'Previous_qualification_grade': [prev_qual_grade],
            'Admission_grade': [admission_grade],
            'Age_at_enrollment': [int(age)],
            'Curricular_units_1st_sem_enrolled': [int(cu_1st_enrolled)],
            'Curricular_units_1st_sem_approved': [int(cu_1st_approved)],
            'Curricular_units_1st_sem_grade': [cu_1st_grade],
            'Curricular_units_2nd_sem_enrolled': [int(cu_2nd_enrolled)],
            'Curricular_units_2nd_sem_approved': [int(cu_2nd_approved)],
            'Curricular_units_2nd_sem_grade': [cu_2nd_grade],
            'Marital_status_label_single': [marital_single],
            'Application_mode_label_Over 23 years old': [app_mode_over23],
            'Course_label_Informatics Engineering': [course_inf_eng],
            'Course_label_Management (evening attendance)': [course_management_eve],
            'Course_label_Nursing': [course_nursing],
            'Course_label_Social Service': [course_social_service],
            'Previous_qualification_label_Basic education 3rd cycle (9th/10th/11th year) or equiv.': [prev_qual_basic],
            'Previous_qualification_label_Secondary education': [prev_qual_secondary],
            'Gender_label_Male': [gender_male],
            'Scholarship_holder_1': [scholarship],
            'Displaced_1': [displaced],
            'Debtor_1': [debtor],
            'Tuition_fees_up_to_date_1': [tuition_up_to_date]
        }
        
        input_df = pd.DataFrame(features)

        with st.spinner("Analyzing..."):
            try:
                prediction = model.predict(input_df)[0]
                
                if hasattr(model, "predict_proba"):
                    probabilities = model.predict_proba(input_df)[0]
                    prob_str = f"Confidence: {max(probabilities)*100:.1f}%"
                else:
                    prob_str = ""
                    
                st.markdown("### 📊 Prediction Result")
                
                if prediction == 0:
                    st.error(f"🚨 **DROPOUT RISK DETECTED** (Class 0) - {prob_str}")
                    st.warning("This student exhibits markers typical of students who fail to complete their studies.")
                elif prediction == 1:
                    st.success(f"🎓 **ON TRACK / GRADUATE** (Class 1) - {prob_str}")
                    st.info("This student exhibits markers typical of successful academic completion.")
                else:
                    st.info(f"The model predicted class: **{prediction}**")
                    
            except Exception as e:
                st.error(f"Prediction failed. Error: {e}")
