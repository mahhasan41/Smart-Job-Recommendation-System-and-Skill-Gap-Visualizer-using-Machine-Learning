# visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Show bar chart of job match scores
def show_match_scores(df):
    st.subheader("📊 Match Score for Top Jobs")
    plt.figure(figsize=(10, 4))
    plt.barh(df['job_title'], df['similarity'], color='skyblue')
    plt.xlabel("Match Score")
    plt.ylabel("Job Title")
    plt.gca().invert_yaxis()
    st.pyplot(plt.gcf())
    plt.clf()

# Show missing skills in a table
def show_missing_skills(missing_skills):
    if missing_skills:
        st.subheader("⚠️ Missing Skills")
        df = pd.DataFrame(missing_skills, columns=["Missing Skill"])
        st.table(df)
        st.info("Consider learning these skills to increase your match accuracy.")
    else:
        st.success("✅ Your skills match all job requirements!")
