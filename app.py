import streamlit as st

st.title("🔦 Flashlight")

if 'on' not in st.session_state:
    st.session_state.on = False

if st.button('ON / OFF', use_container_width=True):
    st.session_state.on = not st.session_state.on

if st.session_state.on:
    st.markdown("<style>.stApp {background-color: white;}</style>", unsafe_allow_html=True)
    st.header("💡 LIGHT ON")
else:
    st.markdown("<style>.stApp {background-color: black;}</style>", unsafe_allow_html=True)
    st.header("🌑 LIGHT OFF")
  
