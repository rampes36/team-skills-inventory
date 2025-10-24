import streamlit as st
import pandas as pd
from modules import crud, visualize, utils

#  page configuration
st.set_page_config(
    page_title="Team Skill Inventory",
)

# ---  Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Add Skill", "View Skills", "Visualize Skills"])

# --- Load Data Function ---
def load_data():
    try:
        df = pd.read_csv("data/skills_data.csv")
        return df
    except FileNotFoundError:
        st.warning("No data file found. Creating a new one...")
        df = pd.DataFrame(columns=["Name", "Skill", "Level"])
        df.to_csv("data/skills_data.csv", index=False)
        return df

# --- Home Page ---
if page == "Home":
    st.title("Team Skill Inventory")
    st.subheader("Welcome to your team's skill tracking dashboard!")
    

# --- Add Skill ---
elif page == "Add Skill":
    st.title("Add a Team Member's Skill")
    st.info("Fill out the form below to add a new skill entry.")
    
    name = st.text_input("Team Member Name")
    skill = st.text_input("Skill")
    level = st.selectbox("Proficiency Level", ["Beginner", "Intermediate", "Expert"])
    
    if st.button("Save Skill"):
        crud.add_skill(name, skill, level)
        st.success(f"{name}'s skill '{skill}' added successfully!")

elif page == "View Skills":
    st.title("Team Skills Database")

    df = crud.read_skills()

    if df.empty:
        st.info("Skills record not found yet. Add one from the 'Add Skill' page.")
    else:
        # ---- Search box ----
        st.subheader("Search Skills")
        query = st.text_input("Enter a name or skill to search:")
        results = crud.search_skills(query)

        # filtered results
        st.dataframe(results, use_container_width=True) 

        # ---- Delete section ----
        st.subheader("Delete a Skill Record")
        if not results.empty:
            delete_index = st.number_input(
                "Enter the index number of the row to delete:",
                min_value=0,
                max_value=len(results) - 1,
                step=1
            )
            if st.button("Delete Selected Record"):
                crud.delete_skill(delete_index)

# --- Visualize Skills ---
elif page == "Visualize Skills":
    st.title("Skill Distribution")
    df = pd.read_csv("data/skills_data.csv")
    if not df.empty:
        visualize.skill_charts(df)
    else:
        st.warning("No data available for visualization.")