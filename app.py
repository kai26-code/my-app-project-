import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #fb2b53;
    }
    </style>
    """,
    unsafe_allow_html=True
)
col_title , col_logo = st.columns([3, 1])

with col_title:
    st.title("📚 Productivity App For Accountants & Students")

