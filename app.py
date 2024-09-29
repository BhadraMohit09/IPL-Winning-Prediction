import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Lucknow Super Giants',
 'Gujarat Titans'
 ]

cities = ['Melbourne Cricket Ground, Melbourne',
'The Oval, London',
'Sydney Cricket Ground, Sydney',
'Old Trafford Cricket Ground, Manchester',
'Lords, London',
'Adelaide Oval, Adelaide',
'St Georges Park, Gqeberha',
'Newlands Cricket Ground, Cape Town',
'Old Wanderers, Johannesburg',
'Trent Bridge, Nottingham',
'Headingley Cricket Ground, Leeds',
'Edgbaston Cricket Ground, Birmingham',
'Bramall Lane, Sheffield',
'Lords No. 1 Ground, Durban',
'Kingsmead Cricket Ground, Durban',
'Brisbane Exhibition Ground, Brisbane',
'Lancaster Park, Christchurch',
'Kensington Oval, Bridgetown',
'Basin Reserve, Wellington',
'Queens Park Oval, Port of Spain',
'Eden Park, Auckland',
'Bourda, Georgetown',
'Sabina Park, Kingston',
'The Gabba, Brisbane',
'Bombay Gymkhana Ground, Mumbai',
'Eden Gardens, Kolkata',
'M. A. Chidambaram Stadium, Chennai',
'Arun Jaitley Stadium, New Delhi',
'Brabourne Stadium, Mumbai',
'Ellis Park Stadium, Johannesburg',
'Green Park Stadium, Kanpur',
'University Ground, Lucknow',
'Bangabandhu National Stadium, Dhaka',
'Bahawal Stadium, Bahawalpur',
'Bagh-e-Jinnah, Lahore',
'Peshawar Club Ground, Peshawar',
'National Stadium, Karachi',
'Carisbrook, Dunedin',
'Lal Bahadur Shastri Stadium, Hyderabad',
'Jawaharlal Nehru Stadium, Chennai',
'New Wanderers Stadium, Johannesburg',
'Gaddafi Stadium, Lahore',
'Pindi Club Ground, Rawalpindi',
'Vidarbha Cricket Association Ground, Nagpur',
'WACA Ground, Perth',
'Niaz Stadium, Hyderabad',
'M. Chinnaswamy Stadium, Bangalore',
'Wankhede Stadium, Mumbai',
'Iqbal Stadium, Faisalabad',
'McLean Park, Napier',
'Ibn-e-Qasim Bagh Stadium, Multan',
'Antigua Recreation Ground, St. Johns',
'Paikiasothy Saravanamuttu Stadium, Colombo',
'Asgiriya Stadium, Kandy',
'Gandhi Stadium, Jalandhar',
'Narendra Modi Stadium, Ahmedabad',
'Singhalese Sports Club Cricket Ground, Colombo',
'Colombo Cricket Club Ground, Colombo',
'Jinnah Stadium, Sialkot',
'Barabati Stadium, Cuttack'
]


pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Match Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling team',sorted(teams))

city = st.selectbox('Select Venue',sorted(cities))

col3,col4 = st.columns(2)

with col3:
    score = st.number_input('Current Score')
with col4:
    wickets = st.number_input('Wickets out')

overs = st.number_input('Overs completed')

target = st.number_input('Target')


if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    # st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
