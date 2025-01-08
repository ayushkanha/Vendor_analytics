import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json
# from reume_page import resume
# from experience_page import experience
# from project_page import projects
# from contact_form import contact
from datainput import datainput
from analytics import analytics
 # Page setup
st.set_page_config(
    page_title="Ayush",
    page_icon="📋",
    layout="wide",
)


def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)

      

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




# Display logo in the sidebar

with st.sidebar:
    # Other sidebar elements
    # st.sidebar.image("logo_image.png", width=200, use_column_width=True)
    # Option menu in sidebar
    pages = ["Input Data", "Analytics"]
    nav_tab_op = option_menu(
        menu_title="Ayush",
        options=pages,
        icons=['person-fill', 'file-text'],
        menu_icon="cast",
        default_index=0,
    )
# # Main content of the app
if nav_tab_op == "Input Data":
    datainput()

elif nav_tab_op == "Analytics":
    analytics()
# elif nav_tab_op == "Experience":
#     experience()
# elif nav_tab_op == "Projects":
#     projects()
# elif nav_tab_op == "Contact":
#     contact()


