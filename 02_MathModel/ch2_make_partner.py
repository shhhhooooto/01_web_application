import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# ==========================
# 初期設定
st.latex("1人以上から好かれる確率: 1 - (1 - p)^n")
def P_loved(n, p):
    return 1 - (1 - p)**n
# ==========================

# 出会う異性の数 (人)
n_min, n_max, n0 = 0, 300, 10
n = st.slider("出会う異性の数: n", n_min, n_max, n0)

# p: 1人から好かれる確率（%）
perc_min, perc_max, perc0 = 0, 100, 1
p = st.slider("1人の異性から好かれる確率(%): p", perc_min, perc_max, perc0)

st.write(f"n={n}, p={p}")

# 1人以上から好かれる確率 = 1 - (1 - p)^n
st.write(f"1人以上の異性から好かれる確率: {P_loved(n, p)}")

if st.button('Print'):

    # ==========================
    dperc = 1
    x_p = np.linspace(perc_min, perc_max, dperc)
    y_p = {P_loved(n, p) for p in x_p}
    y_p = np.array(list(y_p))

    # plt.title(f"y={a}x+{b}")
    plt.text(0.3, 0.3, "O", fontsize=10, ha='center', va='center')
    plt.plot(x_p, y_p, color="r", linewidth=2)
    plt.xlim(perc_min, perc_max)
    plt.ylim(0, 1)
    plt.xticks(np.arange(perc_min, perc_max + dperc, dperc))
    plt.yticks(np.arange(0, 1 + dperc, dperc))
    plt.axhline(0, color='black', lw=1) #  x軸
    plt.axvline(0, color='black', lw=1) #  y軸
    plt.grid()
    st.pyplot(plt)