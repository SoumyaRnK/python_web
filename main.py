import streamlit as st


st.title("Welcome")
st.header("Helooo where are we")
st.markdown("I love python")
st.code(""" for i in range(1,2,1):
    print(i)""")

name=st.text_input("Enter your name")
fname=st.text_input("Enter your first name")
lname=st.text_input("Enter your last name")
age=st.text_input("Enter your age")
adress=st.text_input("Enter your address")
classdata=st.text_input("Enter your class")

button=st.button("Done")

if button:
    st.markdown("""
    Name: {name}
    Fname: {fname}
    Lname: {lname}
    Age: {age}
    Address: {address}
    Class: {classdata}
    """)
