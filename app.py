import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Time Budget Planner", layout="wide")

st.markdown(
    """
    <style>
    .stApp 
        background-color: #f5f7fa;
    
    </style>
    """,
    unsafe_allow_html=True
)

col_title, col_logo = st.columns([3, 1])

with col_title:
    st.title("Productivity App for Accountants & Students")

st.write(
    "Track your weekly time like a financial budget. Input hours you will or have already spent each day in the week.\n In the Category Allocation section, you can distribute your total hours among the three categories.\nClick on Run Analysis to view results & recommendations."
)

st.header("Enter Your Weekly Time")

mon = st.number_input("Monday", min_value=0.0, value=0.0)
tue = st.number_input("Tuesday", min_value=0.0, value=0.0)
wed = st.number_input("Wednesday", min_value=0.0, value=0.0)
thu = st.number_input("Thursday", min_value=0.0, value=0.0)
fri = st.number_input("Friday", min_value=0.0, value=0.0)
sat = st.number_input("Saturday", min_value=0.0, value=0.0)
sun = st.number_input("Sunday", min_value=0.0, value=0.0)

goal = st.number_input("Weekly Goal (Hours)", min_value=0.0, value=0.0)

priority = st.radio(
    "Main Focus This Week",
    ["Study", "Work", "Personal"]
)

st.header("Category Allocation")

study_hours = st.number_input("Study Hours", min_value=0.0, value=0.0)
work_hours = st.number_input("Work Hours", min_value=0.0, value=0.0)
personal_hours = st.number_input("Personal Hours", min_value=0.0, value=0.0)

productive_hours = st.number_input("Productive Hours", min_value=0.0, value=0.0)
improvement = st.slider("Expected Improvement (%)", 0, 100, 0)
hourly_value = st.number_input("Value of Your Time ($/hour)", min_value=0.0, value=0.0)

difficulty = st.selectbox("Workload Level", ["Low", "Moderate", "High"])

run = st.button("Run Analysis")

if run:

    total_hours = mon + tue + wed + thu + fri + sat + sun
    average_hours = total_hours / 7 if total_hours > 0 else 0

    variance = total_hours - goal
    total_value = total_hours * hourly_value

    roi = (improvement / 100 * total_value) / total_hours if total_hours > 0 else 0

    efficiency = (productive_hours / total_hours) * 100 if total_hours > 0 else 0

    needed = goal - total_hours


    st.header("Summary Dashboard")

    st.write(f"Main Focus: {priority}")
    st.write(f"Total Hours: {total_hours:.2f}")
    st.write(f"Average per Day: {average_hours:.2f}")
    st.write(f"Estimated Time Value: ${total_value:.2f}")
    st.write(f"Efficiency: {efficiency:.1f}%")
    st.write(f"Study ROI: {roi:.2f}")   
    st.header("Budget vs Actual Analysis")

    st.write(f"Variance: {variance:.2f} hours")

    if variance > 0:
        st.success("Favorable variance (above target)")
    elif variance < 0:
        st.warning("Unfavorable variance (below target)")
    else:
        st.info("Exact target achieved!")
    if total_hours < goal:
        st.warning("You are below your weekly target.")
    else:
        st.success("You met or exceeded your weekly target.")


    st.header("Break-Even Analysis")

    if needed > 0:
        st.warning(f"You need {needed:.1f} more hours to reach your goal.")
    else:
        st.success("You have met or exceeded your goal!")

    st.header("Recommendations")

    if difficulty == "High" and total_hours < 25:
        st.warning("High workload detected — consider increasing structured hours.")
    elif difficulty == "Low" and total_hours > 25:
        st.info("Low workload — you may be over-allocating time.")
    else:
        st.success("Your schedule looks balanced.")
    if efficiency < 50:
        st.warning("Low efficiency — reduce distractions.")
    elif efficiency > 80:
        st.success("High efficiency — great time management!")

    st.header("Weekly Time Distribution")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = [mon, tue, wed, thu, fri, sat, sun]

    fig1, ax1 = plt.subplots(figsize=(6, 3))  # width, height
    ax1.bar(days, hours)
    ax1.set_title("Hours per Day")
    st.pyplot(fig1)

    st.header("Time Allocation by Category")
    categories = ["Study", "Work", "Personal"]
    values = [study_hours, work_hours, personal_hours]

    total = sum(values)

    if total <= 0:
        st.warning("Please enter category hours to view distribution.")
    else:
        fig2, ax2 = plt.subplots(figsize=(4, 4))
        ax2.pie(values, labels=categories, autopct='%1.1f%%')
        st.pyplot(fig2) 
