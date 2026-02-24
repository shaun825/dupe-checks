import streamlit as st
import pathlib

st.set_page_config(layout="wide", page_title="Invoice Comparator")

html = pathlib.Path("invoice-comparator.html").read_text()
st.components.v1.html(html, height=950, scrolling=True)
