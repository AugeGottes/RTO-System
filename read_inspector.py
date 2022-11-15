import pandas as pd
import streamlit  as st
from database  import view_inspector

def read_inspector():
    result = view_inspector()  # this is defined in the database.py and it basically selects
    df = pd.DataFrame(result, columns=['id','Name'])
    with st.expander("View inspector"):
        st.dataframe(df)