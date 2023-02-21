import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

data_url = ('gs://streamlit-bcfb2.appspot.com/cvs/results.csvhttps://firebasestorage.googleapis.com/v0/b/streamlit-bcfb2.appspot.com/o/cvs%2Fresults.csv?alt=media&token=2c1f5ad1-dc29-4c79-89c6-eede1cd62b7f')

@st.cache 
def load_data():
    data = pd.read_csv(data_url)
    return data

@st.cache
def load__data_bysex(sex):
    data = pd.read_csv(data_url)
    filtered__data_bysex = data[data[ 'sex'] == sex]
    return filtered__data_bysex

data = load_data()

selected_sex = st.selectbox( " Select Sex", data['sex' ].unique())
btnfilterbysex = st.button("Filter by sex")

if (btnfilterbysex):
    filterbysex = load__data_bysex(selected_sex)
    count_row = filterbysex.shape[0] # Gives number of rows
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbysex)