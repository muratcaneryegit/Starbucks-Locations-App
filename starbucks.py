import pandas as pd
import streamlit as st
store=pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")
countries=list(store['country'].unique())
countries.insert(0,"All Countries")
country=st.sidebar.selectbox("Select Country",countries)

if country=="Tüm Ülkeler":
    df=store
else:
    df=store[store['country']==country]
    cities=list(df['city'].unique())
    cities.insert(0,"All Cities")
    city=st.sidebar.selectbox("Select City",cities)
    if city!="All Cities":
        df=df[df['city']==city]



st.map(df)

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.sidebar.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )