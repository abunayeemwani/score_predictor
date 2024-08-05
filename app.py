import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('./model.pkl', 'rb'))

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka',
]

cities = [
    'Colombo',
    'Mirpur',
    'Johannesburg',
    'Dubai',
    'Auckland',
    'Cape Town',
    'London',
    'Pallekele',
    'Barbados',
    'Sydney',
    'Durban',
    'St Lucia',
    'Wellington',
    'Melbourne',
    'Lauderhill',
    'Hamilton',
    'Centurion',
    'Abu Dhabi',
    'Manchester',
]

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
    
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))
    
city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
    
with col4:
    overs = st.number_input('Overs (works for overs > 5)')
    
with col5:
    wickets_lost = st.number_input('Wickets Lost')
    
last_five = st.number_input('Runs scored in last five overs')

if st.button('Predict Score'):
    balls = (int(str(overs).split(".")[0]))*6 + int(str(overs).split(".")[1])
    balls_left = 120 - balls
    crr = (current_score / balls) * 6
    wickets_left = 10 -wickets_lost
    
    input_df = pd.DataFrame(
        {
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': city,
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five],
        }
    )
    
    result = pipe.predict(input_df)
    st.header(f"Predicted Score = {int(result[0])}")
    