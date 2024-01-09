import folium
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium

def custom_styles():
    st.markdown(
        """
        <style>
        .wide-block {
            padding-left: 50px;
            padding-right: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def map_page():
    m = folium.Map(location=[45.8038, 126.5340], zoom_start=10)
    Draw(export=True).add_to(m)

    st.markdown("<div class='map-container'>", unsafe_allow_html=True)

    output = st_folium(m, width=700, height=500)
    st.write(output)

    st.markdown("</div>", unsafe_allow_html=True)

# 其他相关的代码
