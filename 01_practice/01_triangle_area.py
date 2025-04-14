import streamlit as st

st.title("三角形の面積")
st.header("header")
st.subheader("subheader")
st.text("text")
st.markdown("markdown")
st.latex (r"""\frac{1}{2} \times \text{base} \times \text{height}""")

value = st.slider("数値を選んでね", 0, 100, 50)

st.write(f"あなたが選んだ数値の2倍は {value * 2} です！")


if st.button('Click Me'):
    st.write("You clicked the button!")

agree = st.checkbox('I agree')
if agree:
    st.write("You agreed!")

selection = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {selection}")

slider_value = st.slider("Select a range", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

