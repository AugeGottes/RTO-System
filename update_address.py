import pandas as pd
import streamlit as st
from database import view_address
from database import update_data_address
def update_address():
    result = view_address()
    df = pd.DataFrame(result, columns=['aadhar', 'street', 'city', 'state_code'])
    with st.expander("View citizen"):
        st.dataframe(df)
    col1, col2 = st.columns(2)
    with col1:
        aadhar = st.text_input("Enter aadhar details")
    with col2:
        street = st.text_input("Enter street details quick")
        city = st.text_input("Enter city")
        state_code = st.text_input("Enter state code quick")
    if st.button("add address "):
        update_data_address(aadhar, street, city, state_code)