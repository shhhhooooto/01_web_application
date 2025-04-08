import streamlit as st

if st.button('Click Me'):
    st.write("You clicked the button!")

agree = st.checkbox('I agree')
if agree:
    st.write("You agreed!")

selection = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {selection}")

slider_value = st.slider("Select a range", 0, 100, 50)
st.write(f"Slider value: {slider_value}")
