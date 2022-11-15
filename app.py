import streamlit as st
import pandas as pd
from create_citizen import create_citizen
from read_citizen import read_citizen
from delete_citizen import delete_citizen
from database import garbage
from create_address import create_address
from read_adress import read_address
from create_dl import create_dl
from create_inspector import create_inspector
from read_inspector import read_inspector
from create_license import create_license

def main():
    st.title("Rto system")
    st.subheader("Created by Debanjan Das PES1UG20CS119")
    inspector=0
    #
    if st.button("press if you are a citizen"):
        inspector=10
        st.write("hello loser")
    if st.button("press if you are inspector"):
        inspector=11
        st.write("enter password")

    # not inspector case

    menu=["Citizen", "address", "Garbage","apply for dl","Inspector","Driving license"]
    choice=st.sidebar.selectbox("Menu", menu)
    if choice == "Citizen":

        st.subheader("Citizen details")
        citizen_menu=["Add","View","Update","Delete"]
        citizen_choice=st.selectbox("Menu",citizen_menu)
        if citizen_choice=="Add":
            st.subheader("Enter details")
            create_citizen()
        elif citizen_choice=="View" :
            read_citizen()
        elif citizen_choice=="Update" and inspector==11:
            st.write("do the update hathi")
        elif citizen_choice=="Delete" and inspector==11:
            delete_citizen()

    elif choice=="address":
        inspector=10
        st.subheader("Add address")
        address_menu=["Add","View"]
        address_choice=st.selectbox("Menu",address_menu)
        if address_choice=="Add":
            st.subheader("enter details")
            create_address()

            #call the add function for address addtion
        elif address_choice=="View" :
            # st.subheader("view baby")
            read_address()
            #call the view function
    elif choice=="apply for dl":
        st.write("apply for dl")
        create_dl()
    elif choice=="Inspector":
        inspector_menu=["Add","View"]
        citizen_choice=st.selectbox("Menu",inspector_menu)
        if citizen_choice=="Add":
            create_inspector()
        elif citizen_choice=="View":
            read_inspector()
    elif choice=="Driving license":
        license_inspector=["Add","View"]
        license_choice=st.selectbox("Menu",license_inspector)
        if license_choice=="Add":
            create_license()
        elif license_choice=="View":
            read_license()
    elif choice == "Garbage":
            garbage()


if __name__ == "__main__":
    main()