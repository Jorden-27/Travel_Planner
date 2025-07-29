import streamlit as st
from agents import plan_trip

st.set_page_config(page_title="🧠 Travel Task Planner")
st.title("🧠 AI-Powered Task Automation Agent")

st.subheader("Enter your travel details")

destination = st.text_input("Destination", "Lonavala")
duration = st.number_input("Trip Duration (days)", min_value=1, value=7)
budget = st.number_input("Total Budget (INR)", min_value=1000, step=500, value=20000)
num_people = st.number_input("Number of People", min_value=1, value=1)
start_date = st.date_input("Start Date")

if st.button("Generate Plan"):
    with st.spinner("Planning your trip..."):
        final_plan = plan_trip(destination, duration, budget, num_people, start_date)
        st.success("Plan Ready!")
        st.markdown(final_plan)