import streamlit as st
from linear import showData 

if 'score' not in st.session_state:
    st.session_state['score'] = 0
st.title("Other")
showData("./data/other")