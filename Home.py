import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os

df=pd.read_csv("pub_cleaned.csv")


st.set_page_config(page_title="Pub App",
                   layout="centered")


st.title(":red[Open Pub Application🍻]")
image = Image.open('image_3.jpg')
st.image(image, use_column_width=True)

st.markdown("## :red[About the Dataset]")

st.markdown("###### :black[Top Five Rows of Dataset]")
st.write(df.head())

st.markdown("### :red[Total Numbers of Rows and Columns]")
st.write(":black[Total number of Pubs:]", df.shape[0])
st.write(":black[Total number of columns:]", df.shape[1])


st.markdown("### :red[Total number of pub locations in dataset]")
st.write(f':black[{len(df)}]')

st.write(":black[Number of unique local authorities:]", df["local_authority"].nunique())
st.write(":black[Number of unique postal codes:]", df["postcode"].nunique())