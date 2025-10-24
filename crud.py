import pandas as pd
import streamlit as st
import os

DATA_PATH = "data/skills_data.csv"

def add_skill(name, skill, level):
    """Add a new team member skill entry"""
    
    if not name or not skill:
        st.error("Please fill in all fields before saving.")
        return
    
    # Create new entry
    new_entry = pd.DataFrame([[name.strip(), skill.strip(), level]],
                             columns=["Name", "Skill", "Level"])


    if not os.path.exists(DATA_PATH):
        df = pd.DataFrame(columns=["Name", "Skill", "Level"])
        df.to_csv(DATA_PATH, index=False)

    # Add new entry
    df = pd.read_csv(DATA_PATH)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

    st.success(f"{name}'s skill '{skill}' added successfully!")


import pandas as pd
import streamlit as st
import os

DATA_PATH = "data/skills_data.csv"


# ---------- READ FUNCTION ----------
def read_skills():
    """Read all skill records from the CSV file."""
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=["Name", "Skill", "Level"])

    try:
        df = pd.read_csv(DATA_PATH)
        if df.empty or list(df.columns) != ["Name", "Skill", "Level"]:
            df = pd.DataFrame(columns=["Name", "Skill", "Level"])
            df.to_csv(DATA_PATH, index=False)
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return pd.DataFrame(columns=["Name", "Skill", "Level"])


# ---------- SEARCH FUNCTION ----------
def search_skills(query):
    """Filter skills by name"""
    df = read_skills()
    if query:
        query = query.lower()
        df = df[df.apply(lambda row: query in row.astype(str).str.lower().to_string(), axis=1)]
    return df


# ---------- DELETE FUNCTION ----------
def delete_skill(index_to_delete):
    """You can delete one skill record using its row index."""
    df = read_skills()
    if 0 <= index_to_delete < len(df):
        df = df.drop(index_to_delete).reset_index(drop=True)
        df.to_csv(DATA_PATH, index=False)
        st.success("Skill deleted successfully!")
    else:
        st.error("Invalid row number selected for deletion.")    