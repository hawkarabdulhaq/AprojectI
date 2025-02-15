import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
import sys
from streamlit_folium import st_folium
from utils.style1 import set_page_style
from style import show_footer
import sqlite3
from github_sync import push_db_to_github
from datetime import datetime

def update_grade(db_path, username, grade):
    """Simple and direct grade update function"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get current grade first
        cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
        current_grade = cursor.fetchone()
        
        # Update grade
        cursor.execute("""
            UPDATE records 
            SET as1 = ?
            WHERE username = ?
        """, (grade, username))
        
        conn.commit()
        
        # Verify update
        cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
        new_grade = cursor.fetchone()
        
        conn.close()
        return True, current_grade[0] if current_grade else None
    except Exception as e:
        if 'conn' in locals():
            conn.close()
        return False, str(e)

def show():
    # [Previous code remains the same until the submit button section]

    # Submit Code Button
    submit_button = st.button("Submit Code", key="submit_code_button")
    if submit_button:
        if not st.session_state.get("run_success", False):
            st.error("Please run your code successfully before submitting.")
        elif st.session_state.get("username", ""):
            try:
                # Grade the submission
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)
                
                # Get current time
                current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                
                # Update grade
                success, previous_grade = update_grade(
                    db_path, 
                    st.session_state["username"], 
                    grade
                )

                if success:
                    # Show previous grade if it exists
                    if previous_grade is not None:
                        st.info(f"Previous grade: {previous_grade}/100")

                    # Push to GitHub
                    try:
                        push_db_to_github(db_path)
                        st.success(f"""
                        Submission successful! 
                        New grade: {grade}/100
                        Submitted at: {current_time}
                        Submitted by: Hakari-Bibani
                        """)
                    except Exception as e:
                        st.warning("Grade updated locally but failed to sync with GitHub.")
                        st.error(f"GitHub sync error: {str(e)}")
                else:
                    st.error(f"Failed to update grade: {previous_grade}")

                    # Debug information
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    cursor.execute("SELECT as1 FROM records WHERE username = ?", 
                                 (st.session_state["username"],))
                    current_db_grade = cursor.fetchone()
                    st.write(f"Current grade in database: {current_db_grade[0] if current_db_grade else 'None'}")
                    conn.close()

            except Exception as e:
                st.error(f"An error occurred during submission: {str(e)}")

        else:
            st.error("Please enter your username to submit.")

    show_footer()

if __name__ == "__main__":
    show()
