import pandas as pd
import  streamlit as st
from database import view_dl
def read_dl():
    result=view_dl()
    df = pd.DataFrame(result, columns=['aadhar','pname','edate','e_id','dl_id','dl_status'])
    with st.expander("Driving license"):
        st.dataframe(df)