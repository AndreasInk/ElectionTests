import streamlit as st
from linear import showData 

if 'score' not in st.session_state:
    st.session_state['score'] = 0
st.title("Political")
showData("./data/political")

