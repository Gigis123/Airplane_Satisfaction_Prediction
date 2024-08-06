import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title = 'Airline Survey - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Making the title
    st.title('Airline Survey Prediction Model')

    # making the Subheader
    st.subheader('Exploratory Data Analysis for the result of the Airline Survey')

    # adding picture
    st.image('https://static.vecteezy.com/system/resources/thumbnails/015/400/665/small/flying-plane-above-the-clouds-aircraft-in-the-sky-travel-concept-illustration-for-advertising-airline-website-to-search-for-air-tickets-travel-agency-traveling-flyer-banner-illustration-vector.jpg',
             caption= 'Airline Banner - source from google')
    
    # adding Deskripsi
    st.write('-'*50)
    st.write('Milestone 2')
    st.write('Nama  : Achmad Abdillah Ghifari')
    st.write('Batch : BSD-006')
    st.write('-'*50)
    st.write('### OBJECTIVE')
    st.write('we want to create a prediction model in order to help the airline predict the satisfaction of a customer after using their services to find out whether the customer will leave a positive or negative comment. this exploratory data analysis is done in order help improve the services of the airline in order to achieve an overall 90% customer satisfaction score. This is done by finding factors that affect a customer satisfaction and improving it which will increase customer retention and positive comment which in turn will bring more customers and profits for the airline.')
    st.write('**(Please use the submenu on the left to navigate to the relevant feature that has been explored using exploratory data analysis)**')
    st.write('-'*50)
    data = pd.read_csv('Airplane Dataset.csv')
    data = data.drop('Unnamed: 0', axis=1)
    data.satisfaction = data.satisfaction.replace('neutral or dissatisfied',  0)
    data.satisfaction = data.satisfaction.replace('satisfied', 1)

    submenu = st.sidebar.selectbox('Submenu',['Survey Data','Flight Distance','Customer Type', 'Age', 'Class', 'Type of Travel', 'satisfaction'])
    if submenu=="Survey Data":
        st.write('## Data Info')
        with st.expander("Data Description"):
            st.subheader("Data Description")
            st.dataframe(data) 
            st.write(f"Shape of DataFrame is:- {data.shape}")
        with st.expander("Data Types"):
            st.write('## Data Types')
            st.dataframe(data.dtypes)
        with st.expander("Descriptive Table"):
            st.write('## Descriptive Table')
            data = data.drop(['id','Gender','Customer Type','Type of Travel','Class'], axis=1)
            data_describe = data.describe(include='all').fillna("").astype("str")
            st.write(data_describe)
    
    elif submenu=='Flight Distance':
        st.write('### Histogram of Flight Distance')
        fig = plt.figure(figsize=[15,5])
        sns.histplot(data['Flight Distance'], kde=True, bins = 30)
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. The distribution of the flight distance is highly positively skewed. meaning that the airline customer usually travel short distance')
            st.write('2. most of the airline customers travel around 300 KM. from this data we can infer that most travel happen domestically')
            st.write('3. customer rarely travel above 3000 km. this means that while the airline mostly does domestic travle they also do international flight but a bit rarely')
            st.write('from the insight of this data we can see that the airline customer mostly travel a small flight rather than long  flight. from this data, we can conclude that most of the airline data is mostly domestic flight with only some international flight.')

        st.write('### Barchart of Flight Distance and Satisfaction')
        fig = plt.figure(figsize=[15,5])
        sns.barplot(data=data, x='satisfaction', y='Flight Distance',)
        plt.legend(labels=['0 = neutral or dissatisfaction', '1 = satisfaction'])
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. customer with higher flight distance (internationally) at an average of 1500km usually is satisfied with the airline services')
            st.write('2. customer with lower flight distance (domestically) at an average of 900km usually is not satisfied with the airline services')
            st.write('from the insight of this data we can conclude that customer is far more satisfied on long flight distance or international flight rather than shorter distance or domestic flight. we can infer that this happens as the customers that travel internationally usually fly more and have experienced the quality of multiple aircraft compared to people that travel domestically.')

    elif submenu=='Customer Type':
        st.write('### Barchart of Customer Type and Satisfaction')
        fig = plt.figure(figsize=[15,5])
        sns.barplot(data=data, x='Customer Type', y='satisfaction',)
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. loyal customer is usually satisfied with the airline services with an average of around 0.5 satisfaction')
            st.write('2. disloyal customer is usually more dissatisfied with the airline Service with an average of around 0.25 satisfaction')
            st.write('from the insight of this data we can conclude that loyal customer seems to be more satisfied with the airline Service compared to disloyal customer. This could happen as loyal customer can get benefits such as faster queueing and more baggage space.')

    elif submenu=='Age':
        st.write('### satisfaction of age')
        Sex_Bal= data.groupby(['Age', 'satisfaction']).size().unstack(fill_value=0)
        fig, ax = plt.subplots(figsize=[15, 5])
        Sex_Bal.plot(kind='line', ax=ax)
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. dissatisfied customer mostly come from customers around the age 25 and become significantly lower at age 40')
            st.write('2. satisfied customer mostly come from customers around the age 40 and become significantly lower at age 60')
            st.write('from the insight of this data we can conclude that most of the dissatisfied review come from younger customer around the age of 25 and significantly lower at the older age of 40 where people start to give more satisfied review. this could happen as younger audience might prioritize feauture such as online booking and wifi which older audience might not care about much and prefer feature such as comfortable seat and legroom.')

    elif submenu=='Class':
        st.write('### Barchart of Class and Satisfaction')
        fig = plt.figure(figsize=[15,5])
        sns.barplot(data=data, x='Class', y='satisfaction',)
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. customer in business class significantly have higher satisfaction at an average satisfaction of 0.7 compared to both the economy class')
            st.write('2. customer in economy and economy class have a lower satisfaction at around 0.2 to 0.25')
            st.write('from the insight of this data we can conclude that people in business class usually have higher overall satisfaction compared to both economy class. this could happen as the airline business class usually have extra benefit such as a more comfortable chair, better food and drinks, priority baggage and queue, and more compared to economy or economy plus.')

    elif submenu=='Type of Travel':
        st.write('### The amount of Travel Type')
        fig = plt.figure(figsize=[15,5])
        data['Type of Travel'].value_counts().plot(kind='bar')
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. most of the airline customer use the airline for business travel purpose with around 70000 customers')
            st.write('2. only some of the airline customer use the airline for personal travel purpose with around 35000 customers')
            st.write('from the insight of this data we can conclude that most people use the airline for business travel purposes and rarely uses them for personal travel purpose. This could happen because due to the airline high price, people might pick the airline if their work pay for their travel expense.')

    elif submenu=='satisfaction':
        st.write('### Pie chart of satisfaction')
        fig = plt.figure(figsize=[30,10])
        data['satisfaction'].value_counts().plot(kind='pie')
        plt.legend(labels=['0 = neutral or dissatisfaction', '1 = satisfaction'])
        st.pyplot(fig)
        with st.expander("Insight"):
            st.write('1. customer are mostly dissatisfied with the current service of the airline at a total of 56.67%')
            st.write('2. despite most customers is dissatisfied with the airline service. the data is almost balanced between satisfied and dissatisfied')
            st.write('from the insight of this data we can conclude that most of the airline consumers are dissatisfied with our current service. this could happen because as we can see from the flight history, most people travel domestically and most domestic flight customer is dissatisfied.')



if __name__ == '__main__':
    run()