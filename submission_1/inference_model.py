import pandas as pd
import joblib
import xgboost as xgb

class EmployeeAttritionPredictor:
    def __init__(self, model_path='xgb_model.joblib'):
        """
        Inisialisasi predictor dengan memuat model XGBoost yang sudah dilatih.
        """
        try:
            self.model = joblib.load(model_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File model tidak ditemukan di '{model_path}'. Pastikan file berada di direktori yang benar.")

        self.expected_features = [
            'Age',
            'EnvironmentSatisfaction',
            'JobInvolvement',
            'JobLevel',
            'MonthlyIncome',
            'StockOptionLevel',
            'TotalWorkingYears',
            'YearsAtCompany',
            'YearsInCurrentRole',
            'YearsWithCurrManager',
            'BusinessTravel_Travel_Frequently',
            'JobRole_Laboratory Technician',
            'JobRole_Sales Representative',
            'MaritalStatus_Single',
            'OverTime_Yes'
        ]

    def predict(self, input_data):
        """
        Memprediksi status atrisi untuk data input yang diberikan.
        Menerima input berupa dictionary tunggal atau list of dictionaries.
        """

        if isinstance(input_data, dict):
            df = pd.DataFrame([input_data])
        elif isinstance(input_data, list):
            df = pd.DataFrame(input_data)
        else:
            df = input_data.copy()

        for feature in self.expected_features:
            if feature not in df.columns:
                df[feature] = 0
                
        df = df[self.expected_features].astype(int)

        predictions = self.model.predict(df)
        probabilities = self.model.predict_proba(df)[:, 1] # Mengambil probabilitas untuk Kelas 1 (Atrisi)

        results = []
        for pred, prob in zip(predictions, probabilities):
            results.append({
                "Attrition_Prediction": int(pred),
                "Attrition_Probability": float(prob),
                "Risk_Level": "High" if prob >= 0.5 else "Low" 
            })
            
        return results

# ==========================================
# Blok Pengujian (Example Usage)
# ==========================================
if __name__ == "__main__":
    predictor = EmployeeAttritionPredictor(model_path='xgb_model.joblib')

    sample_employees = [
        {
            # Karyawan 1: Berisiko Tinggi (Muda, gaji rendah, lembur, single)
            'Age': 24,
            'EnvironmentSatisfaction': 1,
            'JobInvolvement': 2,
            'JobLevel': 1,
            'MonthlyIncome': 2000,
            'StockOptionLevel': 0,
            'TotalWorkingYears': 1,
            'YearsAtCompany': 1,
            'YearsInCurrentRole': 0,
            'YearsWithCurrManager': 0,
            'BusinessTravel_Travel_Frequently': 1,
            'JobRole_Laboratory Technician': 1,
            'JobRole_Sales Representative': 0,
            'MaritalStatus_Single': 1,
            'OverTime_Yes': 1
        },
        {
            # Karyawan 2: Berisiko Rendah (Senior, gaji tinggi, stabil, tidak lembur)
            'Age': 45,
            'EnvironmentSatisfaction': 4,
            'JobInvolvement': 3,
            'JobLevel': 4,
            'MonthlyIncome': 15000,
            'StockOptionLevel': 2,
            'TotalWorkingYears': 20,
            'YearsAtCompany': 10,
            'YearsInCurrentRole': 8,
            'YearsWithCurrManager': 8,
            'BusinessTravel_Travel_Frequently': 0,
            'JobRole_Laboratory Technician': 0,
            'JobRole_Sales Representative': 0,
            'MaritalStatus_Single': 0,
            'OverTime_Yes': 0
        }
    ]

    print("Mengeksekusi Prediksi...\n")
    results = predictor.predict(sample_employees)
    
    for i, res in enumerate(results):
        print(f"Karyawan {i+1}:")
        print(f" - Prediksi Atrisi: {res['Attrition_Prediction']} (1=Yes, 0=No)")
        print(f" - Probabilitas   : {res['Attrition_Probability']:.2f}")
        print(f" - Tingkat Risiko : {res['Risk_Level']}\n")