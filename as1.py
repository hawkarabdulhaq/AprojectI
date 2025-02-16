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
from datetime import datetime

def push_db_to_github(db_path: str):
    """Push database changes directly to GitHub"""
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    branch = "main"
    file_path = db_path
    api_url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    try:
        # First, make sure the local database is properly closed
        # to ensure all changes are written to disk
        with open(db_path, "rb") as f:
            content = f.read()
        encoded_content = base64.b64encode(content).decode("utf-8")
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Get current file's SHA
        get_response = requests.get(api_url, headers=headers)
        sha = get_response.json().get("sha") if get_response.status_code == 200 else None

        # Prepare and send update
        commit_message = f"Database update: {datetime.now().isoformat()}"
        data = {
            "message": commit_message,
            "content": encoded_content,
            "branch": branch,
        }
        if sha is not None:
            data["sha"] = sha

        put_response = requests.put(api_url, headers=headers, json=data)
        return {"success": put_response.status_code in [200, 201]}
    except Exception as e:
        return {"success": False, "error": str(e)}

def update_grade_and_sync(username: str, grade: float, db_path: str):
    """Update grade in database and sync with GitHub"""
    success = False
    error_message = None
    
    try:
        # Ensure proper database connection and update
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Update grade
        cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (grade, username))
        conn.commit()
        
        if cursor.rowcount == 0:
            error_message = "No record updated. Please check the username."
        else:
            # Verify the update
            cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
            result = cursor.fetchone()
            
            if result and result[0] == grade:
                # Close connection before pushing to GitHub
                conn.close()
                
                # Push to GitHub
                push_result = push_db_to_github(db_path)
                
                if push_result.get("success"):
                    success = True
                else:
                    error_message = f"GitHub sync failed: {push_result.get('error', 'Unknown error')}"
            else:
                error_message = "Grade verification failed"
                
    except Exception as e:
        error_message = f"Database operation failed: {str(e)}"
    finally:
        try:
            conn.close()
        except:
            pass
            
    return success, error_message

def show():
    # Apply the custom page style
    set_page_style()

    # Initialize session state variables
    if "run_success" not in st.session_state:
        st.session_state["run_success"] = False
    if "map_object" not in st.session_state:
        st.session_state["map_object"] = None
    if "dataframe_object" not in st.session_state:
        st.session_state["dataframe_object"] = None
    if "captured_output" not in st.session_state:
        st.session_state["captured_output"] = ""
    if "username_entered" not in st.session_state:
        st.session_state["username_entered"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""

    # Define the database path
    db_path = st.secrets["general"]["db_path"]

    # [Previous code remains the same until the submit button section]

    submit_button = st.button("Submit Code", key="submit_code_button")
    if submit_button:
        if not st.session_state.get("run_success", False):
            st.error("Please run your code successfully before submitting.")
        elif st.session_state.get("username", "").strip():
            from grades.grade1 import grade_assignment
            grade = grade_assignment(code_input)

            st.info("Updating grade and syncing with GitHub...")
            
            success, error_message = update_grade_and_sync(
                st.session_state["username"], 
                grade, 
                db_path
            )

            if success:
                st.success(f"Submission successful! Your grade: {grade}/100")
            else:
                st.error(f"Submission failed: {error_message}")

            # Clear the username state
            st.session_state["username_entered"] = False
            st.session_state["username"] = ""
        else:
            st.error("Please enter your username to submit.")

if __name__ == "__main__":
    show()
