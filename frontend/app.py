import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from backend.data_ingestion import load_google_fit_data
from backend.storage import store_data_locally

# Page setup
st.set_page_config(page_title="AI Life OS - Dashboard", page_icon="⚡️", layout="centered")
st.title("⚡️ AI Life OS - Dashboard")

# Intro Section
st.write("""
Welcome to your AI Life OS dashboard!  
Here, you will soon see your productivity, health, and emotional wellness insights.  
Stay tuned for the upcoming features.
""")
st.info("Start journaling and syncing your activity to unlock personalized coaching!")
st.markdown("---")

# === Load and Display Data ===
data = load_google_fit_data()
stored = store_data_locally(data)

# Section: Steps
st.header("📊 Daily Steps")
for step in stored.get("steps", []):
    st.write(f"{step['date']}: {step['count']} steps")

# Section: Sleep
st.header("🛌 Sleep Tracker")
for sleep in stored.get("sleep", []):
    st.write(f"{sleep['date']}: {sleep['duration_minutes']} minutes, Quality: {sleep['quality']}")

# Section: Heart Rate
st.header("❤️ Heart Rate")
for hr in stored.get("heart_rate", []):
    st.write(f"{hr['date']}: Resting HR: {hr['resting_hr']} bpm, Max HR: {hr['max_hr']} bpm")

# Section: Calories
st.header("🔥 Calories Burned")
for cal in stored.get("calories", []):
    st.write(f"{cal['date']}: {cal['burned']} kcal")

# Footer
st.markdown("---")
st.markdown("© 2025 Tayseer Farooq | Open Source - Privacy First")
