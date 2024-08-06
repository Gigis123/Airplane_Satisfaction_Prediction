import pandas as pd
import numpy as np
import pickle
import streamlit as st
with open('model_xgb.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

def run():
    with st.form("my_form"):
        st.write("## Airplane Satisfaction Survey")
        st.write('Dear valued passenger, Airline strive to give the best flight experience to our passenger and we would like to hear your experience flying with us. rest assured your feedback will help us enchance our service to provide the best flight experience. Thank you for taking the time to fill in this survey ')

        st.write('## Personal Information')
        id = st.number_input('What is your id number?', 0, 10000000000, 100, help= 'id number refer to the number on your identification card')
        gender = st.selectbox('What is your gender?', ['Male', 'Female'], index=0, help= "please select the gender you identify as")
        cust_type = st.selectbox('How many time have you fly with us this month?', ['less than 3 flights', 'more than or equal to 3 flights'], index=1, help= 'please select the amount of time you fly with us this month')
        if cust_type == 'less than 3 flights':
            customer = 'disloyal Customer'
        else:
            customer = 'Loyal Customer'
        age = st.number_input('What is your age?', 18, 100, 30, help= 'please select your current age (age should be between 18-100 years)')
        trav_type = st.selectbox('What is the purpose of your travel?', ['Business travel', 'Personal Travel'], index=1, help= 'please select the purpose of your trip')
        fl_class = st.selectbox('What is the purpose of your travel?', ['Business', 'Eco', 'Eco Plus'], index=1, help= 'please select the travel class you choose for this flight')
        distance = st.number_input('How long was your trip', 30, 5000, 850, help= 'please select the distance of your trip (if you dont know give estimates)')
        
        st.write('## Satisfaction Survey')
        wifi = st.slider('on a scale from 1 to 5, how satisfied are you with our inflight wifi service', 0, 5, 5, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        time = st.slider('on a scale from 1 to 5, how satisfied are you with our departure/arrival time convenient', 0, 5, 3, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied)')
        on_booking = st.slider('on a scale from 1 to 5, how satisfied are you with our ease of online booking', 0, 5, 5, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        gate_loc = st.slider('on a scale from 1 to 5, how satisfied are you with our gate location distance', 0, 5, 3, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied)')
        fnd = st.slider('on a scale from 1 to 5, how satisfied are you with our selection of inflight food and drink', 0, 5, 2, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        on_boarding = st.slider('on a scale from 1 to 5, how satisfied are you with our online boarding service', 0, 5, 4, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        seat_com = st.slider('on a scale from 1 to 5, how satisfied are you with our inflight seat comfortability', 0, 5, 1, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied)')
        fl_entertainment = st.slider('on a scale from 1 to 5, how satisfied are you with our selection of inflight entertainment', 0, 5, 3, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        on_board = st.slider('on a scale from 1 to 5, how satisfied are you with our on-board service', 0, 5, 2, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        leg_room = st.slider('on a scale from 1 to 5, how satisfied are you with your seats legroom', 0, 5, 2, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied)')
        bag_hand = st.slider('on a scale from 1 to 5, how satisfied are you with the handling of your baggage', 0, 5, 4, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        checkin = st.slider('on a scale from 1 to 5, how satisfied are you with our check-in process', 0, 5, 5, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied)')
        inflight = st.slider('on a scale from 1 to 5, how satisfied are you with our selection of inflight service', 0, 5, 4, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied), pick 0 if you dont experience this service')
        clean = st.slider('on a scale from 1 to 5, how satisfied are you with the cleanliness of our plane', 0, 5, 3, help='please select how satisfied are you from 1(very unsatisfied) to 5(very satisfied)')
        dep_delay = st.number_input('Did you experience any delay on your departure? if so how long (in minutes)', 0, 2000, 0, help= 'please input the amount of departure delay you experienced in minutes (if no delay please input 0, if delay more than 2000 minute input 2000)')
        arr_delay = st.number_input('Did you experience any delay on your arrival? if so how long (in minutes)', 0, 2000, 0, help= 'please input the amount of departure delay you experienced in minutes (if no delay please input 0, if delay more than 2000 minute input 2000)')

        submitted = st.form_submit_button("Submit")
        
    data_inf = {
        'id': id,
        'Gender': gender, 
        'Customer Type': customer, 
        'Age': age, 
        'Type Travel': trav_type, 
        'Class': fl_class,
        'Flight Distance': distance, 
        'Wifi': wifi, 
        'Time Convenient': time, 
        'Online Booking': on_booking,
        'Gate location': gate_loc, 
        'Food and drink': fnd, 
        'Online boarding': on_boarding, 
        'Seat comfort': seat_com,
        'Inflight entertainment': fl_entertainment, 
        'On-board service': on_board, 
        'Leg room service': leg_room,
        'Baggage handling': bag_hand, 
        'Checkin service': checkin, 
        'Inflight service': inflight,
        'Cleanliness': clean, 
        'Departure Delay': dep_delay, 
        'Arrival Delay': arr_delay, 
    }

    data_inf = pd.DataFrame([data_inf])

    st.write('-'*50)
    st.write('(Hidden from users)')
    st.write('# Result')
    if submitted:
        result= model.predict(data_inf)
        for i in result:
            if i == 0:
                st.write('### customer is more likely to give a negative comment')
            elif i == 1:
                st.write('### customer is more likely to give a positive comment')
            else:
                st.write('### no data has been inputed')
    st.write('-'*50)

if __name__ =='__main__':
   run()

  