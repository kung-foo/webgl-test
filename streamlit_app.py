import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("WebGL Test")

col1, col2 = st.columns(2)

points = col1.number_input("Points", 1000, 10000)

render_mode = col2.selectbox("Mode", ["svg", "webgl"])

np.random.seed(points) # heh

plot_df = pd.DataFrame.from_dict({"data": np.random.random(points)})

fig = px.line(plot_df, render_mode=render_mode)

st.plotly_chart(fig, use_container_width=True)