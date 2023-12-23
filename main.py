import streamlit as st
import utils as utl
from views import home,chat,search

st.set_page_config(layout="wide", page_title='Chat and Search Bot Interface')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "chat":
        chat.load_view()
    elif route == "search":
        search.load_view()
    elif route == None:
        home.load_view()
        
navigation()