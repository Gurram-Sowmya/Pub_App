import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os

df=pd.read_csv("pub_cleaned.csv")

st.title(":red[Nearest Pub Locations🍺]")
img = Image.open('image_2.jpg')
st.image(img, use_column_width=True)


#Take input latitude and longitude from user
lat=st.number_input(label="Enter your Latitude Here", min_value=49.892485, max_value=60.764969)

long=st.number_input(label="Enter your Longitude Here", min_value=-7.384525, max_value=1.757763)

n_pubs = st.slider('Number of nearest pubs to display:', 1, 10, 5)

def pub():
    x=np.array(df['latitude'])
    y=np.array(df['longitude'])

    df['Distance']=np.sqrt((x-lat)**2+(y-long)**2)

    data=df.sort_values(by='Distance', ascending=True)[:n_pubs].reset_index()
    st.map(data[['latitude', 'longitude']])
    st.table(data[['name','address','local_authority']])
    
st.button("Find nearest pub" ,on_click=pub)