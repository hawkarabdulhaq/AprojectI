import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
from github_sync import push_db_to_github
import time
import os

def update_grade_with_retry(db_path: str, username: str, grade: float):
    """Update grade with retry mechanism and verification"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            conn = sqlite3.connect(db_path, timeout=20)
            cursor = conn.cursor()
            
            # Set immediate transaction mode
            cursor.execute("PRAGMA immediate_transactions = ON")
            
            # Begin transaction
            cursor.execute("BEGIN IMMEDIATE")
            
            # Update grade
            cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (grade, username))
            
            # Verify update
            cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
            result = cursor.fetchone()
            
            if result and abs(result[0] - grade) < 0.01:
                cursor.execute("COMMIT")
                conn.commit()
                return True, None
            else:
                cursor.execute("ROLLBACK")
                if attempt < max_retries - 1:
                    time.sleep(1)
                continue
                
        except sqlite3.Error as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            return False, f"Database error: {str(e)}"
        finally:
            try:
                conn.close()
            except:
                pass
    
    return False, "Failed to update grade after multiple attempts"

def show():
    # [Previous initialization code remains the same]

    submit_button = st.button("Submit Code", key="submit_code_button")
    if submit_button:
        if not st.session_state.get("run_success", False):
            st.error("Please run your code successfully before submitting.")
        elif st.session_state.get("username", "").strip():
            from grades.grade1 import grade_assignment
            grade = grade_assignment(code_input)

            st.info("Updating grade...")
            
            # Update local database
            success, error_message = update_grade_with_retry(
                st.secrets["general"]["db_path"],
                st.session_state["username"],
                grade
            )

            if success:
                st.info("Grade updated locally. Pushing to GitHub...")
                # Push to GitHub
                push_result = push_db_to_github(st.secrets["general"]["db_path"])
                
                if push_result.get("success"):
                    st.success(f"Submission successful! Your grade: {grade}/100")
                else:
                    st.error(f"GitHub sync failed: {push_result.get('error', 'Unknown error')}")
            else:
                st.error(f"Failed to update grade: {error_message}")

            # Clear the username state
            st.session_state["username_entered"] = False
            st.session_state["username"] = ""
        else:
            st.error("Please enter your username to submit.")

if __name__ == "__main__":
    show()
