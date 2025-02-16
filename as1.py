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
from datetime import datetime

# --- Integrated GitHub Push Function ---
def push_db_to_github(db_file: str):
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    branch = "main"  # Adjust if your default branch is different
    file_path = db_file  # Ensure this path matches your repo structure
    api_url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    try:
        with open(db_file, "rb") as f:
            content = f.read()
        encoded_content = base64.b64encode(content).decode("utf-8")
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Get the current file's SHA (if it exists)
        get_response = requests.get(api_url, headers=headers)
        if get_response.status_code == 200:
            sha = get_response.json().get("sha")
        else:
            sha = None

        commit_message = f"Database update: {datetime.now().isoformat()}"
        data = {
            "message": commit_message,
            "content": encoded_content,
            "branch": branch,
        }
        if sha is not None:
            data["sha"] = sha

        put_response = requests.put(api_url, headers=headers, json=data)
        if put_response.status_code in [200, 201]:
            return {"success": True}
        else:
            return {"success": False, "error": put_response.json()}
    except Exception as e:
        return {"success": False, "error": str(e)}

# ----------------- Main App Function -----------------
def show():
    # Apply the custom page style
    set_page_style()

    # (Initialization of session_state variables … remains unchanged)
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

    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")
    # ... (Steps 1 & 2 code remains unchanged) ...

    # Step 3: Run and Submit Your Code
    st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: white;">📝 Paste Your Code Here</p>', unsafe_allow_html=True)
    code_input = st.text_area("", height=300)

    run_button = st.button("Run Code", key="run_code_button")
    if run_button and code_input:
        st.session_state["run_success"] = False
        st.session_state["captured_output"] = ""
        try:
            from io import StringIO
            import sys

            captured_output = StringIO()
            sys.stdout = captured_output

            local_context = {}
            exec(code_input, {}, local_context)

            sys.stdout = sys.__stdout__

            st.session_state["captured_output"] = captured_output.getvalue()

            map_object = next((obj for obj in local_context.values() if isinstance(obj, folium.Map)), None)
            dataframe_object = next((obj for obj in local_context.values() if isinstance(obj, pd.DataFrame)), None)

            st.session_state["map_object"] = map_object
            st.session_state["dataframe_object"] = dataframe_object

            st.session_state["run_success"] = True
        except Exception as e:
            sys.stdout = sys.__stdout__
            st.error(f"An error occurred while running your code: {e}")

    if st.session_state["run_success"]:
        st.markdown('<h3 style="color: white;">📄 Captured Output</h3>', unsafe_allow_html=True)
        if st.session_state["captured_output"]:
            formatted_output = st.session_state["captured_output"].replace('\n', '<br>')
            st.markdown(f'<pre style="color: white; white-space: pre-wrap; word-wrap: break-word;">{formatted_output}</pre>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color: white;">No text output captured.</p>', unsafe_allow_html=True)

        if st.session_state["map_object"]:
            st.markdown("### 🗺️ Map Output")
            st_folium(st.session_state["map_object"], width=1000, height=500)

        if st.session_state["dataframe_object"] is not None:
            st.markdown("### 📊 DataFrame Output")
            st.dataframe(st.session_state["dataframe_object"])

    # ---- Updated Submit Code Section ----
    submit_button = st.button("Submit Code", key="submit_code_button")
    if submit_button:
        if not st.session_state.get("run_success", False):
            st.error("Please run your code successfully before submitting.")
        elif st.session_state.get("username", "").strip():
            from grades.grade1 import grade_assignment
            grade = grade_assignment(code_input)

            try:
                # Use a context manager to update the database
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE records SET as1 = ? WHERE username = ?",
                        (grade, st.session_state["username"])
                    )
                    conn.commit()
                    updated_rows = cursor.rowcount

                if updated_rows == 0:
                    st.error("No record updated. Please check the username or database integrity.")
                else:
                    st.info("Grade updated locally. Pushing changes to GitHub...")
                    # Add a short delay to ensure changes are flushed to disk
                    time.sleep(0.5)
                    response = push_db_to_github(db_path)
                    if response.get("success"):
                        with sqlite3.connect(db_path) as conn:
                            cursor = conn.cursor()
                            cursor.execute("SELECT as1 FROM records WHERE username = ?", (st.session_state["username"],))
                            result = cursor.fetchone()
                        if result:
                            new_grade = result[0]
                            st.success(f"Submission successful! Your grade: {new_grade}/100")
                        else:
                            st.error("Error retrieving the updated grade after push.")
                    else:
                        st.error(f"GitHub push failed: {response.get('error')}")
            except Exception as e:
                st.error(f"Error updating the database: {str(e)}")

            # Clear username state so the user must re-enter it for the next submission
            st.session_state["username_entered"] = False
            st.session_state["username"] = ""
        else:
            st.error("Please enter your username to submit.")

if __name__ == "__main__":
    show()
