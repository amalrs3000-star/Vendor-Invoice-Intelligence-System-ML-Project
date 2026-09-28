# 🧾 Vendor Invoice Intelligence System
### AI-Powered Freight Cost Prediction & Invoice Risk Flagging

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Database](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> An end-to-end Machine Learning system that helps finance teams predict freight costs and automatically flag risky vendor invoices for manual review.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Business Objectives](#-business-objectives)
- [Data Sources](#️-data-sources)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Models Used](#-models-used)
- [Evaluation Metrics](#-evaluation-metrics)
- [ML Workflow](#-machine-learning-workflow)
- [Streamlit Application](#️-streamlit-application)
- [Project Structure](#-project-structure)
- [Tech Stack](#️-tech-stack)
- [How to Run](#️-how-to-run-this-project)
- [Results](#-results--insights)
- [Future Improvements](#-future-improvements)
- [Author](#-author--contact)

---

## 📖 Project Overview

This project implements a **complete end-to-end Machine Learning pipeline** to solve two critical finance problems:

1.  **Freight Cost Prediction (Regression):** Accurately forecasts the expected freight cost for any vendor invoice.
2.  **Invoice Risk Flagging (Classification):** Automatically detects invoices with unusual financial or operational patterns that require manual approval.

The system extracts data from a relational SQLite database, performs EDA and statistical testing, trains and evaluates ML models, and serves predictions through an interactive **Streamlit** web application.

---

## ✨ Key Features
- 📦 **Freight Forecasting:** Predicts freight cost using invoice value & quantity
- 🚩 **Smart Flagging:** Flags high-risk invoices using Random Forest + GridSearchCV
- 📊 **Statistical Validation:** Uses t-tests to validate difference between flagged vs normal invoices
- 🔍 **Interactive UI:** Real-time prediction with Streamlit
- 💾 **Production Ready:** Model persistence with Joblib & clean inference pipeline

---

## 🎯 Business Objectives

### 1. Freight Cost Prediction
**Objective:** Predict the expected freight cost associated with a vendor invoice.

**Business Impact:**
- Improves budgeting and landed cost estimation
- Supports procurement planning and vendor negotiation
- Helps identify abnormal freight charges early

### 2. Invoice Risk Flagging
**Objective:** Identify invoices with unusual patterns and flag them for additional review.

**Business Impact:**
- Reduces manual invoice verification workload
- Prevents financial leakage in large/complex invoices
- Increases audit efficiency and operational control

---

## 🗄️ Data Sources

Data is stored in `inventory.db` (SQLite) and queried using SQL aggregations.

| Table | Description |
| :--- | :--- |
| `vendor_invoice` | Invoice-level financial and timing data |
| `purchases` | Item-level purchase details |
| `purchase_prices` | Reference purchase prices |
| `begin_inventory` | Beginning inventory snapshot |
| `end_inventory` | Ending inventory snapshot |

> Note: `inventory.db` is excluded from GitHub due to large file size and is stored locally.

---

## 📊 Exploratory Data Analysis

EDA was focused on business-driven questions:

- Does freight scale linearly with invoice value?
- Do flagged invoices have higher financial exposure?
- Does receiving delay correlate with invoice risk?
- How do total item quantity and dollars vary between flagged vs normal?

**Tools:** Pandas, Matplotlib, Seaborn, Statistical t-tests

### 📈 Statistical Analysis
Independent two-sample t-tests were performed to confirm significant differences between flagged and non-flagged invoices for:
- `invoice_quantity`, `invoice_dollars`, `Freight`
- `days_from_PO_to_invoice`, `days_to_pay`
- `total_item_quantity`, `total_item_dollars`

---

## 🤖 Models Used

### 🚚 Freight Prediction (Regression)
- **Baseline:** Linear Regression
- **Intermediate:** Decision Tree Regressor
- **Final Model:** Random Forest Regressor

### 🚨 Invoice Flagging (Classification)
- **Model:** Random Forest Classifier
- **Tuning:** GridSearchCV with F1-Score (to handle class imbalance)
- **Features:** `invoice_quantity`, `invoice_dollars`, `Freight`, `total_item_quantity`, `total_item_dollars`

---

## 📏 Evaluation Metrics

**Regression (Freight Prediction)**
- MAE - Mean Absolute Error
- RMSE - Root Mean Squared Error
- R² Score

**Classification (Invoice Flagging)**
- Accuracy, Precision, Recall, F1-Score
- Classification Report
- Feature Importance Analysis

---

## 🔬 Machine Learning Workflow

**Freight Prediction Pipeline:**



---

## 🖥️ Streamlit Application

An interactive web app with 2 modules:

#### 1. Freight Cost Prediction
Enter `Quantity` and `Invoice Dollars` → Get predicted freight cost.

#### 2. Invoice Risk Detection
Enter `Invoice Quantity, Dollars, Freight, Total Quantity, Total Dollars` → Get `MANUAL APPROVAL REQUIRED` or `SAFE for Auto-Approval`.

**Screenshots:**
- `images/app_home.png` - Home Page
- `images/freight_prediction.png` - Freight Module
- `images/invoice_risk_detection.png` - Risk Flagging Module

---

## 📁 Project Structure

---

## 🛠️ Tech Stack

**Languages:** Python, SQL
**Data:** Pandas, NumPy, SQLite
**ML:** Scikit-Learn, Random Forest, GridSearchCV
**Visualization:** Matplotlib
**Deployment:** Streamlit, Joblib
**Tools:** Jupyter, Git & GitHub

---

## ▶️ How to Run This Project

**1. Clone the Repository**
```bash
git clone https://github.com/amalrs3000-star/Machine-Learning-Project-1-Vendor-Invoice-Intelligence-System.git
cd Machine-Learning-Project-1-Vendor-Invoice-Intelligence-System
pip install -r requirements.txt
# or
pip install pandas numpy scikit-learn matplotlib joblib streamlit
python Freight_cost_prediction/train.py
python invoice_flagging/train.py
python inference/predict_freight.py
python inference/predict_invoice_flag.py
streamlit run app.py

