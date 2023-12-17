import streamlit as st
import pandas as pd 
import geopandas as gpd
import pydeck as pdk
import seaborn as sns
import h3 as exagon


img = "https://travelnostop.com/wp-content/uploads/2014/02/muqoy_campiflegrei-610x366.jpg"
st.sidebar.image(img)

gdf = gpd.read_file(r"C:\Users\Luigi\Downloads\FW_ODONATA\FW_ODONATA.shp")

tab = pd.read_html("https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes")[0]
tab.columns = tab.columns.droplevel(0)

dict_codes = {}
for row,column in tab.iterrows():
    dict_codes[column["Country name[5]"]] = column["Alpha-3 code[5]"]
  
option = st.selectbox('Select a coutry',list(set(dict_codes.keys())))

st.write('You selected:', option)
