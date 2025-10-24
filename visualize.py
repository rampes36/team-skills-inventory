import streamlit as st
import plotly.express as px
import pandas as pd

def skill_charts(df):
    """Display charts showing the distribution of skills and levels."""
    
    # data confirmtion
    if df.empty:
        st.info("No data to visualize. Add skills first.")
        return

    # Bar Chart
    st.subheader("Skills by Category")
    skill_count = df["Skill"].value_counts().reset_index()
    skill_count.columns = ["Skill", "Count"]

    bar_chart = px.bar(
        skill_count,
        x="Skill",
        y="Count",
        color="Skill",
        title="Skill Distribution",
        text="Count",
        color_discrete_sequence=["#4D96FF", "#9CA3AF", "#E5E7EB", "#F8AFA6", "#FFD93D"]
    )
    st.plotly_chart(bar_chart, use_container_width=True)

    # Pie Chart
    st.subheader("Skill Levels (Beginner / Intermediate / Expert)")
    level_count = df["Level"].value_counts().reset_index()
    level_count.columns = ["Level", "Count"]

    pie_chart = px.pie(
        level_count,
        names="Level",
        values="Count",
        color="Level",
        title="Proficiency Level Breakdown",

        color_discrete_sequence=["#F8AFA6", "#E5E7EB"]
    )
    st.plotly_chart(pie_chart, use_container_width=True)

    # Note for the user
    st.caption("Charts update automatically as you add or delete skills.")