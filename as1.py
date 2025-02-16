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

     st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ──────────────────────────────────────────────────────────────
    # Step 1: Enter Your Username
    # ──────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Username</h1>', unsafe_allow_html=True)
    username_input = st.text_input("Username", key="as1_username")
    enter_username = st.button("Enter")
    if enter_username and username_input:
        # Check in the records table (not the users table)
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
        conn.close()

    if st.session_state.get("username_entered", False):
        # ──────────────────────────────────────────────────────────────
        # Step 2: Review Assignment Details
        # ──────────────────────────────────────────────────────────────
        st.markdown('<h1 style="color: #ADD8E6;">Step 2: Review Assignment Details</h1>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.
            
            **Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python**
            """)
        with st.expander("See More"):
            st.markdown("""
            **Task Requirements:**
            1. **Plot the Three Coordinates on a Map:**
               - The coordinates represent three locations in the Kurdistan Region.
               - Use Python libraries to plot these points on a map.
               - The map should visually display the exact locations of the coordinates.
            2. **Calculate the Distance Between Each Pair of Points:**
               - Calculate the distances between the three points in kilometers.
               - Specifically, calculate:
                 - The distance between Point 1 and Point 2.
                 - The distance between Point 2 and Point 3.
                 - The distance between Point 1 and Point 3.
               - Add markers to the map for each coordinate.
               - Add polylines to connect the points.
               - Add popups to display distance information.
            
            **Coordinates:**
            - Point 1: Latitude: 36.325735, Longitude: 43.928414
            - Point 2: Latitude: 36.393432, Longitude: 44.586781
            - Point 3: Latitude: 36.660477, Longitude: 43.840174
            """)
        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            - **Code Structure and Implementation:** 30 points
            - **Map Visualization:** 40 points
            - **Distance Calculations:** 30 points
            """)
            st.markdown("""
            #### 1. Code Structure and Implementation (30 points)
            - **Library Imports (5 points):**
                - Checks if the required libraries (folium, geopy, geodesic) are imported.
            - **Coordinate Handling (5 points):**
                - Checks if the correct coordinates are defined in the code.
            - **Code Execution (10 points):**
                - Checks if the code runs without errors.
            - **Code Quality (10 points):**
                - **Variable Naming:** 2 points (deducted if single-letter variables are used).
                - **Spacing:** 2 points (deducted if improper spacing is found).
                - **Comments:** 2 points (deducted if no comments are present).
                - **Code Organization:** 2 points (deducted if no blank lines are used for separation).
            """)
            with st.expander("See More"):
                st.markdown("""
                #### 2. Map Visualization (40 points)
                - **Map Generation (15 points):**
                    - Checks if the folium.Map is correctly initialized.
                - **Markers (15 points):**
                    - Checks if markers are added for each coordinate.
                - **Polylines (5 points):**
                    - Checks if polylines connect the points.
                - **Popups (5 points):**
                    - Checks if popups are added to the markers.
                #### 3. Distance Calculations (30 points)
                - **Geodesic Implementation (10 points):**
                    - Checks if the geodesic function is used correctly.
                - **Distance Accuracy (20 points):**
                    - Checks if the calculated distances are accurate within a 100-meter tolerance.
                """)

        # ──────────────────────────────────────────────────────────────
        # Step 3: Run and Submit Your Code
        # ──────────────────────────────────────────────────────────────
        st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">📝 Paste Your Code Here</p>', unsafe_allow_html=True)
        code_input = st.text_area("", height=300)

        # Run Code Button
        run_button = st.button("Run Code", key="run_code_button")
        if run_button and code_input:
            st.session_state["run_success"] = False
            st.session_state["captured_output"] = ""
            try:
                from io import StringIO
                import sys

                captured_output = StringIO()
                sys.stdout = captured_output

                # Execute the user's code in a controlled environment
                local_context = {}
                exec(code_input, {}, local_context)

                # Restore stdout
                sys.stdout = sys.__stdout__

                # Capture printed output
                st.session_state["captured_output"] = captured_output.getvalue()

                # Look for specific outputs (folium.Map, pandas.DataFrame)
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

        # ──────────────────────────────────────────────────────────────
        # Submit Code Button (updates grade and pushes DB)
        # ──────────────────────────────────────────────────────────────

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
