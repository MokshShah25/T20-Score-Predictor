# 🏏 T20 Score Predictor

A Machine Learning web application that predicts the final score of a T20 cricket innings based on the current match situation.

The model uses historical T20 cricket match data and features such as current score, balls bowled, wickets lost, current run rate, and runs scored in the last five overs.

## 🚀 Live Demo

👉 **[T20 Score Predictor](https://t20i-score-predictor.streamlit.app/)**

## 📌 Project Objective

The objective of this project is to predict the probable final score of a T20 cricket innings using Machine Learning.

The prediction is based on the match situation at a particular point in the innings.

## 📊 Input Features

The application takes the following inputs:

- **Batting Team**
- **Bowling Team**
- **City**
- **Current Score**
- **Balls Bowled**
- **Wickets Lost**
- **Current Run Rate (CRR)**
- **Runs Scored in Last 5 Overs**

### Feature Calculations

**Balls Left:**

```text
Balls Left = 120 - Balls Bowled
