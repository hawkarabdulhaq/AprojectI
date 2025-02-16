# as1.py
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
        # Ensure DB is closed and changes are written
        with open(db_path, "rb") as f:
            content = f.read()
        encoded_content = base64.b64encode(content).decode("utf-8")
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Get current SHA
        get_response = requests.get(api_url, headers=headers)
        if get_response.status_code == 200:
            current_sha = get_response.json()["sha"]
            
            # Prepare and send update
            data = {
                "message": f"Database update: {datetime.now().isoformat()}",
                "content": encoded_content,
                "sha": current_sha,
                "branch": branch
            }
            
            put_response = requests.put(api_url, headers=headers, json=data)
            if put_response.status_code in [200, 201]:
                return {"success": True}
            else:
                return {"success": False, "error": f"GitHub API Error: {put_response.status_code}"}
        else:
            return {"success": False, "error": "Failed to get current file SHA"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def verify_database_update(conn, cursor, username: str, expected_grade: float) -> bool:
    """Verify that the grade was properly updated in the database"""
    try:
        cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
        result = cursor.fetchone()
        return result is not None and abs(result[0] - expected_grade) < 0.01
    except Exception:
        return False

def update_grade_and_sync(username: str, grade: float, db_path: str):
    """Update grade in database and sync with GitHub with proper error handling"""
    conn = None
    try:
        # First attempt: Update local database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Update grade with retry mechanism
        max_retries = 3
        for attempt in range(max_retries):
            cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (grade, username))
            conn.commit()
            
            if verify_database_update(conn, cursor, username, grade):
                break
            elif attempt < max_retries - 1:
                # Wait briefly before retry
                import time
                time.sleep(0.5)
        else:
            return False, "Failed to verify database update after multiple attempts"

        # Close connection before GitHub sync
        conn.close()
        conn = None

        # Push to GitHub
        push_result = push_db_to_github(db_path)
        if push_result.get("success"):
            return True, None
        else:
            error_msg = push_result.get("error", "Unknown GitHub sync error")
            return False, f"GitHub sync failed: {error_msg}"

    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"
    finally:
        if conn:
            try:
                conn.close()
            except:
                pass

def show():
    # Apply custom page style
    set_page_style()

    # Initialize session state
    for key in ["run_success", "map_object", "dataframe_object", "captured_output", 
                "username_entered", "username", "last_submission_time"]:
        if key not in st.session_state:
            st.session_state[key] = None if key != "run_success" else False

    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")
    
    # Username Entry Section
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Username</h1>', unsafe_allow_html=True)
    username_input = st.text_input("Username", key="as1_username")
    enter_username = st.button("Enter")
    
    if enter_username and username_input:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM records WHERE username = ?", (username_input,))
            user_record = cursor.fetchone()
            if user_record:
                st.session_state["username_entered"] = True
                st.session_state["username"] = username_input
                st.success(f"Welcome, {username_input}!")
            else:
                st.error("Invalid username. Please enter a registered username.")
                st.session_state["username_entered"] = False
        except Exception as e:
            st.error(f"Database error: {str(e)}")
        finally:
            if 'conn' in locals():
                conn.close()

    if st.session_state.get("username_entered", False):
        # [Previous assignment details and grading sections remain the same]

        st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
        code_input = st.text_area("📝 Paste Your Code Here", height=300)

        # Run Code Button
        if st.button("Run Code", key="run_code_button") and code_input:
            st.session_state["run_success"] = False
            try:
                # Capture output
                captured_output = StringIO()
                import sys
                sys.stdout = captured_output

                # Execute code in controlled environment
                local_context = {}
                exec(code_input, {}, local_context)

                # Restore stdout
                sys.stdout = sys.__stdout__
                st.session_state["captured_output"] = captured_output.getvalue()

                # Check for specific outputs
                st.session_state["map_object"] = next(
                    (obj for obj in local_context.values() if isinstance(obj, folium.Map)), 
                    None
                )
                st.session_state["dataframe_object"] = next(
                    (obj for obj in local_context.values() if isinstance(obj, pd.DataFrame)), 
                    None
                )

                st.session_state["run_success"] = True
            except Exception as e:
                if 'sys' in locals():
                    sys.stdout = sys.__stdout__
                st.error(f"Code execution error: {str(e)}")

        # Display outputs if run was successful
        if st.session_state["run_success"]:
            if st.session_state["captured_output"]:
                st.markdown("### 📄 Output")
                st.text(st.session_state["captured_output"])

            if st.session_state["map_object"]:
                st.markdown("### 🗺️ Map Output")
                st_folium(st.session_state["map_object"], width=1000, height=500)

            if st.session_state["dataframe_object"] is not None:
                st.markdown("### 📊 DataFrame Output")
                st.dataframe(st.session_state["dataframe_object"])

        # Submit Button with Rate Limiting
        current_time = datetime.now()
        can_submit = True
        if st.session_state.get("last_submission_time"):
            time_since_last = (current_time - st.session_state["last_submission_time"]).total_seconds()
            if time_since_last < 10:  # Rate limit: 10 seconds between submissions
                can_submit = False
                st.warning(f"Please wait {10 - int(time_since_last)} seconds before submitting again.")

        submit_button = st.button("Submit Code", key="submit_code_button", disabled=not can_submit)
        
        if submit_button and code_input and st.session_state.get("username", "").strip():
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            else:
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)

                st.info("Processing submission...")
                success, error_message = update_grade_and_sync(
                    st.session_state["username"], 
                    grade, 
                    db_path
                )

                if success:
                    st.success(f"Submission successful! Your grade: {grade}/100")
                    st.session_state["last_submission_time"] = current_time
                else:
                    st.error(f"Submission failed: {error_message}")
                    st.warning("Please try submitting again in a few moments.")

if __name__ == "__main__":
    show()
