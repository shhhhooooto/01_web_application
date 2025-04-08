import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
st.pyplot(plt)

import plotly.express as px
fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6])
st.plotly_chart(fig)