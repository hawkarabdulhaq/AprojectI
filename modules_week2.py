import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# Function to log student activity in mydatabase.db
def log_activity(tab_name):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS activity_log 
                      (timestamp TEXT, tab_name TEXT)''')
    cursor.execute("INSERT INTO activity_log VALUES (?, ?)", 
                   (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tab_name))
    conn.commit()
    conn.close()

def show():
    # List of tab names
    tab_names = [
        "The Scale up Week", "2.1 Breaking Down Scripts!", "2.2 Quiz",
        "2.3 Scale up scripts", "2.4 Merging & Reversing", "2.5 G.C for Researchers",
        "2.6 Case Study", "2.7 Limitations of G.C", "2.8 Google Sheets API",
        "2.9 GitHub for Webapp", "Assignment 3", "Assignment 4"
    ]

    # Create tabs dynamically
    tabs = st.tabs(tab_names)

    # Content for each tab
    with tabs[0]:  # Tab 1: The Scale up Week
        log_activity("The Scale up Week")
        st.header("Welcome to the Scale up Week")
        st.video("https://youtu.be/OC1J2uZlLdQ")

    with tabs[1]:  # Tab 2: Breaking Down Scripts
        log_activity("2.1 Breaking Down Scripts!")
        st.header("2.1 Breaking Down Scripts")
        st.video("https://www.youtube.com/watch?v=fD73oMb4NRg")

    with tabs[2]:  # Tab 3: Quiz
        log_activity("2.2 Quiz")
        st.header("2.2 Python Basics Quiz")
        st.write("Here you can take a short quiz on Python basics.")

    with tabs[3]:  # Tab 4: Scale Up Scripts
        log_activity("2.3 Scale up scripts")
        st.header("2.3 Understanding Python Scripts")
        st.write("A Python script is a set of instructions executed in order.")
        
    with tabs[4]:  # Tab 5: Merging & Reversing
        log_activity("2.4 Merging & Reversing")
        st.header("2.4 Merging & Reversing in Python")
        st.write("Learn how to merge and reverse data efficiently.")

    with tabs[5]:  # Tab 6: G.C for Researchers
        log_activity("2.5 G.C for Researchers")
        st.header("2.5 Google Colab for Researchers")
        st.write("Google Colab is a great tool for researchers.")

    with tabs[6]:  # Tab 7: Case Study
        log_activity("2.6 Case Study")
        st.header("2.6 Case Study on Python Applications")
        st.write("Explore real-world case studies of Python usage.")

    with tabs[7]:  # Tab 8: Limitations of G.C
        log_activity("2.7 Limitations of G.C")
        st.header("2.7 Limitations of Google Colab")
        st.write("Discuss the drawbacks of Google Colab.")

    with tabs[8]:  # Tab 9: Google Sheets API
        log_activity("2.8 Google Sheets API")
        st.header("2.8 Working with Google Sheets API")
        st.write("Learn how to integrate Google Sheets with Python.")

    with tabs[9]:  # Tab 10: GitHub for Webapp
        log_activity("2.9 GitHub for Webapp")
        st.header("2.9 Using GitHub for Your Web Applications")
        st.write("Understand how to integrate GitHub into your projects.")

    with tabs[10]:  # Tab 11: Assignment 3
        log_activity("Assignment 3")
        import as3
        as3.show()

    with tabs[11]:  # Tab 12: Assignment 4
        log_activity("Assignment 4")
        import as4
        as4.show()

if __name__ == "__main__":
    show()
