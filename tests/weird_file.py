import streamlit as st
import numpy as np
import pandas as pd

mp_data = pd.DataFrame(
    np.random.randn(1000 , 2) / [50, 50] + [32.243, -7.9596],
    columns=['lat', 'lon']
)

st.map(mp_data)