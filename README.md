# 🧠 Multiple Disease Prediction System (Diabetes & Heart Disease)

This project uses machine learning models to predict **diabetes** and **heart disease** based on user input health metrics. It provides a simple interface and trained models to assist in early-stage medical predictions.

---

## 📁 Project Structure

```
📦 final diab_heart prediction/
├── diabetes.csv                         # Dataset for diabetes prediction
├── heart.csv                            # Dataset for heart disease prediction
├── diabetes_model.sav                   # Trained model (Diabetes)
├── heart_disease_model.sav              # Trained model (Heart Disease)
├── multiplediseaseprediction.py         # Main prediction script
├── askai.py                             # Chat/assistant integration (optional logic)
├── Multiple Disease Prediction System - Diabetes.ipynb
├── Multiple Disease Prediction System - Heart.ipynb
```

---

## ⚙️ How It Works

1. **Data Preprocessing**:
   - Loads health data from CSV files
   - Normalizes and prepares input features

2. **Model Training**:
   - Trained using classification algorithms (e.g., Logistic Regression, SVM)
   - Saved using `joblib` or `pickle` for reusability

3. **Prediction Logic**:
   - User inputs key health metrics (like BMI, glucose level, age, cholesterol)
   - The model returns `Positive` or `Negative` prediction based on input

---

## 🧪 Requirements

Install required packages:

```bash
pip install numpy pandas scikit-learn matplotlib
```

---

## 🚀 How to Run

Run the main prediction script:

```bash
python multiplediseaseprediction.py
```

Or, explore and test the models through the provided Jupyter Notebooks:

```bash
jupyter notebook
# Open:
# - Multiple Disease Prediction System - Diabetes.ipynb
# - Multiple Disease Prediction System - Heart.ipynb
```

---

## 📊 Datasets

- `diabetes.csv` – Contains medical data relevant to diabetes diagnosis.
- `heart.csv` – Contains medical parameters for heart disease classification.

---

## ✅ Features

- Two-disease support: Diabetes and Heart Disease
- Pre-trained models for instant predictions
- Clean input/output handling in both script and notebook form

---

## 💡 Future Improvements

- Add a web interface using Streamlit or Flask
- Expand to more diseases using multi-label classification
- Include visualization of user data and prediction explanation (e.g., SHAP values)
