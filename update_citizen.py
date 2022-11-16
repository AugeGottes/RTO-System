import pandas as pd
import streamlit as st
from database import update_data_citizen
from database import view_license
def update_citizen():
    result = view_license()
    df = pd.DataFrame(result,
                      columns=['lid', 'aadhar', 'name', 'license_no', 'license_issue_date', 'license_expiry_date'])
    with st.expander("View citizen"):
        st.dataframe(df)
    col1, col2 = st.columns(2)
    with col1:
        firstname = st.text_input("First Name")
        lastname = st.text_input("Last Name")
    with col2:
        aadhar = st.text_input("Enter valid aadhar ")
        gender = st.text_input("Add gender")
        dob = st.date_input("Enter dob")
        phone_no = st.text_input("enter phone no")
    if st.button("Update citizen"):
        update_data_citizen(firstname,lastname,aadhar,gender,dob,phone_no)
        st.success("Successfully updated citizen")