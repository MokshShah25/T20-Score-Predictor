import streamlit as st
import pickle
import pandas as pd


# Load trained model
pipe = pickle.load(open("pipe.pkl", "rb"))


# Teams
teams = [
    "Australia",
    "India",
    "Bangladesh",
    "New Zealand",
    "South Africa",
    "England",
    "West Indies",
    "Afghanistan",
    "Pakistan",
    "Sri Lanka"
]


# Cities
cities = [
    "Colombo",
    "Mirpur",
    "Johannesburg",
    "Dubai",
    "Auckland",
    "Cape Town",
    "London",
    "Pallekele",
    "Barbados",
    "Sydney",
    "Melbourne",
    "Durban",
    "St Lucia",
    "Wellington",
    "Lauderhill",
    "Hamilton",
    "Centurion",
    "Manchester",
    "Abu Dhabi",
    "Mumbai",
    "Nottingham",
    "Southampton",
    "Mount Maunganui",
    "Chittagong",
    "Kolkata",
    "Lahore",
    "Delhi",
    "Nagpur",
    "Chandigarh",
    "Adelaide",
    "Bangalore",
    "St Kitts",
    "Cardiff",
    "Christchurch",
    "Trinidad"
]


# Title
st.title("Cricket Score Predictor")
st.subheader("Format - T20")


# Team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "Select batting team",
        sorted(teams)
    )

with col2:
    bowling_teams = [
        team for team in teams
        if team != batting_team
    ]

    bowling_team = st.selectbox(
        "Select bowling team",
        sorted(bowling_teams)
    )


# City
city = st.selectbox(
    "Select City",
    sorted(cities)
)


# Match information
col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input(
        "Current Score",
        min_value=0,
        max_value=300,
        value=0,
        step=1
    )

with col4:
    balls_bowled = st.number_input(
        "Balls bowled",
        min_value=1,
        max_value=120,
        value=60,
        step=1
    )

with col5:
    wicket = st.number_input(
        "Wickets Lost",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )


# Last five overs
last_five = st.number_input(
    "Runs Scored in last 5 overs",
    min_value=0,
    max_value=100,
    value=0,
    step=1
)


# Prediction
if st.button("Predict Score"):

    # Balls remaining
    balls_left = 120 - balls_bowled

    # Wickets remaining
    wickets_left = 10 - wicket

    # Current run rate
    crr = (current_score * 6) / balls_bowled

    # Create input dataframe
    input_df = pd.DataFrame({
        "batting_team": [batting_team],
        "bowling_team": [bowling_team],
        "city": [city],
        "current_score": [current_score],
        "balls_left": [balls_left],
        "wickets_left": [wickets_left],
        "crr": [crr],
        "last_five": [last_five]
    })

    # Prediction
    result = pipe.predict(input_df)

    # Display result
    st.header("Predicted Score - " + str(int(result[0])))