import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
import requests
import base64
import time

# Inline push function (using GitHub API)
def push_db_to_github(db_path: str):
    try:
        with open(db_path, "rb") as f:
            content = f.read()
    except Exception as e:
        st.error(f"Error reading {db_path}: {e}")
        return

    encoded_content = base64.b64encode(content).decode("utf-8")
    repo = st.secrets["general"]["repo"]    # e.g., "username/reponame"
    token = st.secrets["general"]["token"]
    # Make sure this path matches exactly what is in your GitHub repository.
    url = f"https://api.github.com/repos/{repo}/contents/{db_path}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    get_response = requests.get(url, headers=headers)
    sha = None
    if get_response.status_code == 200:
        sha = get_response.json().get("sha")
    else:
        st.info("Database file not found on GitHub. It will be created.")

    data = {
        "message": f"Update {db_path} at {time.time()}",
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha

    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code not in [200, 201]:
        st.error(f"Error pushing to GitHub: {put_response.status_code} - {put_response.text}")
    else:
        st.success("Database pushed successfully to GitHub!")

def show():
    # Apply custom page style
    set_page_style()

    # IMPORTANT: Do not call create_tables() or any pull function here.
    # We assume mydatabase.db already exists locally and is the authoritative version.
    # Remove any code like:
    #   from database import create_tables
    #   create_tables()

    # Initialize session state variables if not already set.
    if "run_success" not in st.session_state:
        st.session_state["run_success"] = False
    if "username_entered" not in st.session_state:
        st.session_state["username_entered"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""

    # Define your local database path (should match what’s on GitHub)
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # Step 1: Enter Username
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Username</h1>', unsafe_allow_html=True)
    username_input = st.text_input("Username", key="as1_username")
    if st.button("Enter"):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE username = ?", (username_input,))
        user_record = cursor.fetchone()
        conn.close()
        if user_record:
            st.session_state["username_entered"] = True
            st.session_state["username"] = username_input
        else:
            st.error("Invalid username. Please enter a registered username.")
            st.session_state["username_entered"] = False

    # Only show the rest of the app if a valid username is entered.
    if st.session_state.get("username_entered", False):
        # (Assignment details and code runner omitted for brevity.)
        st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
        code_input = st.text_area("📝 Paste Your Code Here", height=300)
        
        if st.button("Run Code", key="run_code_button") and code_input:
            try:
                from io import StringIO
                import sys
                captured_output = StringIO()
                sys.stdout = captured_output
                local_context = {}
                exec(code_input, {}, local_context)
                sys.stdout = sys.__stdout__
                st.session_state["captured_output"] = captured_output.getvalue()
                st.session_state["run_success"] = True
            except Exception as e:
                sys.stdout = sys.__stdout__
                st.error(f"Error while running your code: {e}")

        if st.session_state.get("run_success", False):
            st.markdown('<h3>📄 Captured Output</h3>', unsafe_allow_html=True)
            st.markdown(st.session_state["captured_output"])

        # Submit Code: update grade and push database
        if st.button("Submit Code", key="submit_code_button"):
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            elif st.session_state.get("username", ""):
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)

                # Update the grade in the local DB
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (grade, st.session_state["username"]))
                conn.commit()
                conn.close()

                st.info("Grade updated locally. Pushing changes to GitHub...")
                push_db_to_github(db_path)

                # Verify update by querying local DB
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT as1 FROM records WHERE username = ?", (st.session_state["username"],))
                result = cursor.fetchone()
                conn.close()
                if result and result[0] == grade:
                    st.success(f"Submission successful! Your grade: {result[0]}/100")
                else:
                    st.error("Error retrieving or updating the grade.")
            else:
                st.error("Please enter your username to submit.")

if __name__ == "__main__":
    show()
