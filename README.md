# what-if-simulator
 This project is an interactive machine learning simulator that allows users simulate how different factors affect student performance.

# Student Performance What-If Simulator (ML + Streamlit App)

##  Live Demo

[https://your-streamlit-app-link.streamlit.app](https://your-streamlit-app-link.streamlit.app)

---

##  Project Overview

This project is an interactive **Machine Learning-based simulator** that predicts a student's final exam score based on academic and behavioral factors.

It allows users to explore **what-if scenarios** by adjusting inputs such as:

* Study hours
* Attendance rate
* Past exam performance
* Parental education level
* Internet access at home
* Extracurricular activities

The goal is to demonstrate how different factors influence academic performance using predictive modeling.

---

##  Problem Statement

Students’ academic performance is influenced by multiple behavioral and environmental factors.
This project aims to:

> Build a predictive system that estimates final exam scores and allows users to simulate how changes in behavior affect outcomes.

---

##  Dataset

* Source: Kaggle Educational Performance Dataset
* Samples: ~700 students
* Features:

| Feature                    | Description                   |
| -------------------------- | ----------------------------- |
| Study_Hours_per_Week       | Weekly study time             |
| Attendance_Rate            | Class attendance percentage   |
| Past_Exam_Scores           | Previous academic performance |
| Parental_Education_Level   | Categorical encoded value     |
| Internet_Access_at_Home    | Binary (0/1)                  |
| Extracurricular_Activities | Binary (0/1)                  |
| Final_Exam_Score           | Target variable               |

###  Important Note

The target variable ranges between **50 and 77**, which influences prediction bounds.

---

##  Machine Learning Approach

Two regression models were trained and compared:

### 1. Linear Regression (Baseline)

* Simple interpretable model
* Required feature scaling
* Served as baseline performance

### 2. Random Forest Regressor (Final Model)

* Captures non-linear relationships
* No feature scaling required
* Selected as final deployment model

---

##  Model Performance

| Model             | MAE      | R² Score |
| ----------------- | -------- | -------- |
| Linear Regression | 3.10     | 0.66     |
| Random Forest     | **2.03** | **0.80** |

✔ Random Forest was selected due to superior predictive performance.

---

##  Feature Importance Insight

Key influencing factors observed:

* Past Exam Scores (strongest predictor)
* Study Hours per Week
* Attendance Rate
* Parental Education Level
* Extracurricular Activities

This aligns with real-world educational research findings.

---

##  Web Application

Built using:

* Streamlit

### Features:

* Interactive sliders and input fields
* Real-time predictions
* What-if scenario simulation
* Instant feedback on student performance changes

---

##  Example Scenarios Tested

### High Performer

* High study hours
* High attendance
* Strong past scores
  ➡ Predicted score: ~67–70

### Mid Performer

* Moderate inputs
  ➡ Predicted score: ~52–55

### Low Performer

* Low inputs across features
  ➡ Predicted score: ~50–51 (dataset lower bound)

---

##  Key Limitation

The dataset used has a **compressed target range (50–77)**.
As a result:

* The model does not predict extreme low or high scores
* Outputs are naturally clustered around the dataset mean

This highlights the importance of dataset selection in predictive modeling systems.

---

##  Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Git & GitHub

---

##  Project Structure

```text
what-if-simulator/
│
├── app.py
├── models/
│   ├── random_forest_model.pkl
│   ├── linear_model_scaled.pkl
│
├── data/
├── notebooks/
├── requirements.txt
└── README.md
```

---

##  How to Run Locally

```bash
git clone https://github.com/your-username/what-if-simulator.git
cd what-if-simulator

conda activate whatif

pip install -r requirements.txt

streamlit run app.py
```

---

##  Key Learnings

* End-to-end ML pipeline development
* Model comparison and evaluation
* Feature importance interpretation
* Handling real-world dataset limitations
* Deploying ML apps using Streamlit Cloud
* Debugging environment and dependency issues

---

##  Author

**Onyinye Okpoko**
Aspiring Data Scientist | ML Engineer
GitHub: [https://github.com/OnyeeVeee](https://github.com/OnyeeVeee)

---

##  Future Improvements

* Add classification model (Pass/Fail prediction)
* Add confidence intervals for predictions
* Deploy model API using FastAPI
* Improve dataset with broader score distribution
* Add model comparison toggle in UI

---


