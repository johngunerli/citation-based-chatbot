import streamlit as st
import os
def load_view():
    st.title('Home Page')
    st.write(os.getenv('LOAD_VIEW'))