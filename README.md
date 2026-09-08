
# 🏏 T20 Cricket Score Predictor

A Machine Learning web application that predicts the **final score of a T20 cricket innings** based on the current match situation.

The model uses historical T20 cricket delivery data and features such as current score, balls remaining, wickets remaining, current run rate, and runs scored in the last five overs.

## 🚀 Live Demo

🔗 **[Try the Streamlit App](YOUR_STREAMLIT_APP_URL)**

---

## 📌 Project Overview

Predicting the final score of a T20 innings can help estimate how the current match situation may influence the final score.

This project follows an end-to-end Machine Learning workflow:

- Data extraction from YAML cricket files
- Data cleaning and preprocessing
- Feature engineering
- Model training and comparison
- Match-level train/test evaluation
- ExtraTrees Regression
- Streamlit web application
- Model deployment

---

## 🎯 Objective

The objective of this project is to predict the **final innings score** using the current state of a T20 match.

### Input Features

The application uses:

- 🏏 Batting Team
- 🎯 Bowling Team
- 📍 City
- 📊 Current Score
- 🏃 Balls Bowled
- ❌ Wickets Lost
- ⚡ Current Run Rate (CRR)
- 🔥 Runs Scored in Last 5 Overs

### Output

The model predicts:

> **Expected Final Score of the innings**

---

## 🧠 Machine Learning

This is a **Regression** problem because the target variable, final score, is numerical.

### Models Compared

The following regression models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. Extra Trees Regressor
4. XGBoost Regressor

### Final Model

The application uses:

**ExtraTreesRegressor**

The model is integrated into a Scikit-learn Pipeline containing:

- One-Hot Encoding for categorical features
- ExtraTreesRegressor for prediction

---

## 📊 Features

### Current Score

The total number of runs scored by the batting team so far.

### Balls Left

The number of legal deliveries remaining in the 20-over innings.

For a T20 innings:

```text
Balls Left = 120 - Balls Bowled
```
