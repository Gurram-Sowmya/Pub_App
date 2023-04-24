import streamlit as st
import pandas as pd
import os
from PIL import Image
st.set_page_config(layout="wide")



df = pd.read_csv('pub_cleaned.csv')

st.title(":red[Pub Locations🍺]")
image = Image.open('image_1.jpg')
st.image(image, use_column_width=True)


location_type = st.selectbox(
    "Select the location type:",
    ('Postal Code', 'Local Authority'))

if location_type == 'Postal Code':
    location = st.selectbox('Select the Postal Code:', df['postcode'].unique())
    pubs = df[df['postcode'] == location].reset_index()
else:
    location = st.selectbox('Select Local Authority:', df['local_authority'].unique())
    pubs = df[df['local_authority'] == location].reset_index()
st.write(f'Total number of pubs found in the {location} are {len(pubs)}.')

st.table(pubs[['name','address']])

st.map(pubs[['latitude', 'longitude']])