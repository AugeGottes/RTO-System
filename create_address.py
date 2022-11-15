import streamlit as st
from database import create_table_address
from database import add_data_address

def create_address():
    # col1,col2=st.columns(2)
    # with col1:
    #     aadhar=st.text_input("Enter aadhar details")
    # with col2:
    #     street=st.text_input("Enter street details")
    #     city=st.text_input("Enter city")
    #     state_code=st.text_input("Enter state code")
    # if st.button("add adress"):
    #     create_table_address()
    #     add_data_address(aadhar,street,city,state_code)
    #     st.success("address successfully added")

    with st.form(key="Driving License application form"):
        aadhar=st.text_input("Enter aadhar number")
        street = st.text_input("Enter street details")
        city = st.text_input("Enter city")
        state_code = st.text_input("Enter state code")
        submit_button = st.form_submit_button(label='Submit')