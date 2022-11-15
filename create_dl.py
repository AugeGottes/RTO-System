import streamlit as st
import pandas as pd
import datetime
from database import create_table_dl
from database import add_table_dl


def create_dl():
    col1,col2=st.columns(2)
    with col1:
        aadhar=st.text_input("Enter aadhar number")
        name=st.text_input("Enter name")
        edate=st.date_input("Enter date of application")
    with col2:
        eid=st.text_input("Enter e_id")
        dl_id=st.text_input("Enter dl_id")


    if st.button("Apply for dll"):
        dl_status=0
        create_table_dl()
        add_table_dl(aadhar,name,edate,eid,dl_id,dl_status)
        st.success("successfully added table dl")



