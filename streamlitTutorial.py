# import packages
import streamlit as st  # frontend user interface design
import numpy as np      # scientific calculation
import pandas as pd     # data analysis

st.title("Hello, Streamlit")
st.write("🚀 This is your first streamlit app")
st.text("Let's get started")
st.write("My name is Kalyani Belorkar")

# conditional logic
name = st.text_input("Enter Your Name")
if st.button("Greet"):
    st.success(f"Hello {name}")

# Displaying data and charts
df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.line_chart(df)
st.bar_chart(df)

#File iuploading and caching
upload_file = st.file_uploader("Upload File", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

# all the userinterface of streamlit
st.header("this is a header")
st.markdown("**Bold**, *Italic*, [Link](http://localhost:8501)")
st.text_area("Write your message")
st.number_input("pick a number", min_value=0, max_value=100)
st.slider("choose a range",0, 100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("choose toppings",["cheese","tomato","Olives"])
st.radio("Pick one",["Option A", "Option B"])
st.checkbox("I agree terms and condition")

# form code
with st.form("Login form"):
    username = st.text_input("username")
    password = st.text_input("password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"welcome, {username}")

#Check radio button
option = st.radio("Choose View", ["Show chart", "Show table"])
if option == "Show chart":
    st.write("Chart whould be appear here")
else:
    st.write("Table would be appear here")

if st.checkbox("Show details"):
    st.info("Here are more details")

#Media layout and advance widget
st.sidebar.title("New Chart")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3xYeCI6imAKgNuA5PHmmLO7D4iG4fs-oCHGocrA4v3w&s=10")
st.video("https://youtu.be/rlHy2P9dNus")
