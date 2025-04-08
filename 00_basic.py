import streamlit as st

st.title("簡単なシミュレーション")
value = st.slider("数値を選んでね", 0, 100, 50)
st.write(f"あなたが選んだ数値の2倍は {value * 2} です！")

print("hello world!")