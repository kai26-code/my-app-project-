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

import matplotlib.pyplot as plt

# ----------------------------
# Title & Description
# ----------------------------
st.title("📊 Time Budget Planner")

st.write(
    "This app helps you manage your weekly time like a budget. "
    "Enter your daily hours and compare them to your weekly goal."
)

# ----------------------------
# Inputs
# ----------------------------
st.header("📥 Enter Your Time")

mon = st.number_input("Monday Hours", min_value=0.0)
tue = st.number_input("Tuesday Hours", min_value=0.0)
wed = st.number_input("Wednesday Hours", min_value=0.0)
thu = st.number_input("Thursday Hours", min_value=0.0)
fri = st.number_input("Friday Hours", min_value=0.0)
sat = st.number_input("Saturday Hours", min_value=0.0)
sun = st.number_input("Sunday Hours", min_value=0.0)

goal = st.number_input("🎯 Weekly Goal (Hours)", min_value=0.0)

priority = st.radio(
    "Main Focus This Week",
    ["Study", "Work", "Personal"]
)

# ----------------------------
# Calculations
# ----------------------------
total_hours = mon + tue + wed + thu + fri + sat + sun
average_hours = total_hours / 7 if total_hours > 0 else 0

# ----------------------------
# Dynamic Output
# ----------------------------
st.header("📊 Summary")

st.write(f"Total Hours: {total_hours:.2f}")
st.write(f"Average Hours per Day: {average_hours:.2f}")

st.write(f"Main Focus This Week: {priority}")


