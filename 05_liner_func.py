import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# ==========================
# 初期設定
st.latex("y = ax + b")

# 傾き
a_min, a_max, a0 = -10, 10, 0

# 切片
b_min, b_max, b0 = -10, 10, 0

a = st.slider("a", a_min, a_max, a0)
b = st.slider("b", b_min, b_max, b0)
st.write(f"a={a}, b={b}")

if st.button('Print'):
    # st.write("You clicked the button!")
    # ==========================
    # 表示

    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.plot(x, y)
    st.pyplot(plt)