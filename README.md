# 🚀 Vendor Invoice Intelligence System
### Freight Cost Prediction & Invoice Risk Flagging

An end-to-end machine learning project that combines **SQL, Python, statistical analysis, machine learning, and Streamlit** to analyze vendor invoices, predict expected freight costs, and identify potentially abnormal invoices that may require further review.

---

## 📌 Project Overview

Vendor invoice processing involves analyzing financial, purchasing, and operational information to determine whether invoice amounts are reasonable and whether unusual transactions require additional attention.

This project develops an end-to-end **Vendor Invoice Intelligence System** with two machine learning solutions:

### 1. Freight Cost Prediction

A regression-based machine learning pipeline that predicts the expected freight cost associated with a vendor invoice.

### 2. Invoice Risk Flagging

A classification-based machine learning pipeline that identifies invoices with potentially abnormal financial or operational patterns and flags them for further review.

The project follows a complete machine learning workflow:

```text
Business Problem
      ↓
SQLite Database
      ↓
SQL Data Extraction
      ↓
Data Cleaning & Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Statistical Analysis
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Model Evaluation
      ↓
Hyperparameter Tuning
      ↓
Model Saving
      ↓
Inference
      ↓
Streamlit Application