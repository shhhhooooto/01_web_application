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
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10
    x = np.linspace(x_min, x_max, 100)
    y = a * x + b

    plt.plot(x, y)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.axhline(0, color='black', lw=1) #  x軸
    plt.axvline(0, color='black', lw=1) #  y軸
    plt.grid()
    st.pyplot(plt)