import pandas as pd
import streamlit as st
dukkan=pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")
ulkeler=list(dukkan['country'].unique())
ulkeler.insert(0,"Tüm Ülkeler")
ulke=st.sidebar.selectbox("Ülke Seçiniz:",ulkeler)

if ulke=="Tüm Ülkeler":
    df=dukkan
else:
    df=dukkan[dukkan['country']==ulke]
    sehirler=list(df['city'].unique())
    sehirler.insert(0,"Tüm Şehirler")
    sehir=st.sidebar.selectbox("Şehir Seçiniz",sehirler)
    if sehir!="Tüm Şehirler":
        df=df[df['city']==sehir]



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