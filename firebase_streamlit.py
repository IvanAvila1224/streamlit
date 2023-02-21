import streamlit as st
import pandas as pd

st.title( 'Streamlit - Search ranges')

DATA_URL = ("https://firebasestorage.googleapis.com/v0/b/streamlit-bcfb2.appspot.com/o/imagen%2FScreenshot_20230215_075524.png?alt=media&token=6cb12864-cf64-4b95-b85f-ec0e57d38341")

@st.cache
def load_data_byrange(name):
    data = pd.read_csv (DATA_URL)
    filtered_data_byname = data[data('name').str.contains(name)]
    return filtered_data_byname

myname = st.text_input("Name: ")
if (myname):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0]
    st.write(f"total names: {count_row}")

    st.dataframe(filterbyname)