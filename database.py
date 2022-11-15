import mysql.connector
import streamlit as st
import pandas as pd
mydb = mysql.connector.connect(
host="localhost", user="root", password="", database="rto"
)
c = mydb.cursor()


def create_table_citizen():

    c.execute('create table if not exists citizen(firstname varchar(30),lastname varchar(30),aadhar char(1),gender char(1),dob DATE ,phone_no char(1),PRIMARY KEY (aadhar))')


def add_data_citizen(firstname,lastname,aadhar,gender,dob,phone_no):

    c.execute("insert into citizen(firstname,lastname,aadhar,gender,dob,phone_no) values (%s,%s,%s,%s,%s,%s )",(firstname,lastname,aadhar,gender,dob,phone_no))
    mydb.commit()


def view_citizen():
    c.execute('select * from citizen')
    data = c.fetchall()
    return data


def delete_citizen_db(aadhar):
    c.execute('delete from citizen where aadhar="{}"'.format(aadhar))
    mydb.commit()

def create_table_address():
     c.execute('create table if not exists address(aadhar varchar(10) primary key,street varchar(50),city varchar(30),state_code varchar(30) foreign key(aadhar) references citizen(aadhar))')


def add_data_address(aadhar,street,city,state_code):
    c.execute("insert into address(aadhar,street,city,state_code) values (%s,%s,%s,%s)",(aadhar,street,city,state_code))
    mydb.commit()

def view_address():
    c.execute('select * from address')
    data=c.fetchall()
    return data

def create_table_dl():
    c.execute('create table if not exists dl (aadhar varchar(10),pname varchar(10),edate date,e_id varchar(10),dl_id varchar(10),dl_status char(1))')

def add_table_dl(aadhar,pname,edate,e_id,dl_id,dl_status):
    c.execute("insert into dl(aadhar,pname,edate,e_id,dl_id,dl_status) values (%s,%s,%s,%s,%s,%s)",(aadhar,pname,edate,e_id,dl_id,dl_status))
    mydb.commit()

def create_table_inspector():
        c.execute('create table if not exists inspector (id varchar(10),iname varchar(10),passwd varchar(10),primary key(id))')

def add_data_inspector(id,iname,passwd):
        c.execute("insert into inspector values (%s,%s,%s)",(id,iname,passwd))
        mydb.commit()
def view_inspector():
    c.execute('select id,iname from inspector')
    return c.fetchall()

def create_table_license():
    pass
def garbage():
    txt = st.text_input("enter sql")
    c.execute(txt)
    data=c.fetchall()
    st.write(data)
    # df = pd.DataFrame(data, columns=['First Name', 'Last Name', 'aadhar', 'gob', 'dob', 'pno'])
    # with st.expander("View citizen"):
    #     st.dataframe(df)