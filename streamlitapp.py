import streamlit as st
import pickle
import pandas as pd

# st.write('This is a simple web app to predict the passenger surviving in Titanic')
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title('Passenger Surviviung Prediction App')



Age = st.number_input('Age', min_value=0, max_value=100, value=0)
Passenger_ID = st.number_input('Passenger_ID', min_value=0, max_value=100, value=0)
gender = st.selectbox("Gender", options=["Male", "Female"])
Seat_Type=st.number_input('Seat_Type', min_value=0, max_value=100, value=0)
Class=st.selectbox("Class", options=["First", "Bussiness","Ennonomy"])
Fare_Paid=st.number_input('Fare_Paid', min_value=0, value=0)

input_df = pd.DataFrame({
    'Passenger_ID': [Passenger_ID],
    'Age': [Age],
    'Gender': [gender],
    'Class': [Class],
    'Seat_Type': [Seat_Type],
    'Fare_Paid': [Fare_Paid]
})

# conver the categorical values to numerical values
input_df['Gender'] = input_df['Gender'].map({'Male': 0, 'Female': 1})


input_df["Class"] = input_df["Class"].map({"First":3,"Business":2,"Economy":1})


input_df["Seat_Type"] = input_df["Seat_Type"].map({"Window":3,"Middle":2,"Aisle":1})

align=["Passenger_ID",	"Age"	,"Gender","Class",	"Seat_Type",	"Fare_Paid"]
input_df = input_df.reindex(columns=align)

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_df)
    st.write(f'The predicted survival status is: {"Survived" if prediction[0] == 1 else "Not Survived"}')