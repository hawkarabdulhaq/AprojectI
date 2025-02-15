import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
from style import show_footer  # Added this import
import sqlite3
from github_sync import push_db_to_github
from datetime import datetime

def show():
    # Apply the custom page style
    set_page_style()

    # Initialize session state variables if not already set
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

    # Define the database path from secrets
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ──────────────────────────────────────────────────────────────
    # Step 1: Enter Your Username
    # ──────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Username</h1>', unsafe_allow_html=True)
    username_input = st.text_input("Username", key="as1_username")
    enter_username = st.button("Enter")
    if enter_username and username_input:
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

    if st.session_state.get("username_entered", False):
        # [Previous assignment details code remains unchanged]
        # ... [Include your existing assignment details and tabs code here]

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

        # Submit Code Button
        submit_button = st.button("Submit Code", key="submit_code_button")
        if submit_button:
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            elif st.session_state.get("username", ""):
                try:
                    # Grade the submission using your grading function
                    from grades.grade1 import grade_assignment
                    grade = grade_assignment(code_input)

                    # Connect to database
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()

                    # Get current grade to show difference
                    cursor.execute("SELECT as1 FROM records WHERE username = ?", 
                                 (st.session_state["username"],))
                    current_grade = cursor.fetchone()

                    # Update the grade in the records table
                    cursor.execute("""
                        UPDATE records 
                        SET as1 = ? 
                        WHERE username = ?
                    """, (grade, st.session_state["username"]))
                    
                    conn.commit()
                    updated_rows = cursor.rowcount

                    if updated_rows == 0:
                        st.error("No record updated. Please check the username or database integrity.")
                    else:
                        # Show previous grade if it exists
                        if current_grade and current_grade[0] is not None:
                            st.info(f"Previous grade: {current_grade[0]}/100")
                        
                        # Push changes to GitHub
                        try:
                            push_db_to_github(db_path)
                            st.success(f"Submission successful! Your new grade: {grade}/100")
                        except Exception as e:
                            st.warning("Grade updated locally but failed to sync with GitHub. Please try again later.")
                            st.error(f"GitHub sync error: {str(e)}")

                    conn.close()

                except Exception as e:
                    st.error(f"An error occurred during submission: {str(e)}")
                    if 'conn' in locals():
                        conn.close()
            else:
                st.error("Please enter your username to submit.")

    # Call show_footer() at the end of the function
    show_footer()

if __name__ == "__main__":
    show()
