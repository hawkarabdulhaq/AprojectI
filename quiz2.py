import streamlit as st
import sqlite3
from github_sync import push_db_to_github  # Optional: if you use GitHub sync

# Quiz Questions and Points remain unchanged
questions = [
    {
        "question": "Splitting a script into multiple smaller scripts helps make the code more manageable and easier to debug.",
        "points": 35,
        "answer": True
    },
    {
        "question": "The main.py script is responsible for importing and executing functions or modules stored in other scripts saved on Google Drive.",
        "points": 35,
        "answer": True
    },
    {
        "question": "Saving smaller scripts in Google Drive and importing them into Google Colab increases the risk of altering the main script when making changes.",
        "points": 30,
        "answer": False
    }
]

MAX_ATTEMPTS = 1

def add_custom_css():
    st.markdown("""
        <style>
        /* (CSS remains unchanged) */
        </style>
    """, unsafe_allow_html=True)

def validate_username(username):
    try:
        db_path = st.secrets["general"]["db_path"]
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE username = ?", (username,))
        record = cursor.fetchone()
        conn.close()
        return record is not None
    except Exception as e:
        st.error(f"Error validating username: {e}")
        return False

def show():
    add_custom_css()
    
    st.title("Quiz 2: Python and Script Management")
    
    # Step 1: Enter Username
    with st.container():
        st.markdown("<h2 style='color: #ADD8E6;'>Step 1: Enter Your Username</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            username = st.text_input("Username", placeholder="Enter your username")
        with col2:
            verify_button = st.button("Verify Username")
    
    if "quiz2_attempts" not in st.session_state:
        st.session_state["quiz2_attempts"] = 0

    if verify_button:
        if validate_username(username):
            st.success("✅ Username validated. You can proceed with the quiz.")
            st.session_state["validated"] = True
            st.session_state["verified_username"] = username
        else:
            st.error("❌ Invalid username. Please enter a registered username.")
            st.session_state["validated"] = False

    if st.session_state.get("validated", False):
        # Step 2: Answer Questions
        st.markdown("<h2 style='color: #ADD8E6;'>Step 2: Answer the Questions</h2>", unsafe_allow_html=True)

        if "user_answers_quiz2" not in st.session_state:
            st.session_state["user_answers_quiz2"] = [None] * len(questions)

        for i, question in enumerate(questions):
            with st.container():
                st.markdown(f"""
                    <div class="question-container">
                        <div class="question-text">
                            Q{i+1}: {question['question']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                answer = st.radio(
                    "",
                    options=["True", "False"],
                    key=f"question_quiz2_{i}",
                    horizontal=True,
                    label_visibility="collapsed"
                )
                st.session_state["user_answers_quiz2"][i] = answer == "True"

        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submit_button = st.button(
                "Submit Quiz",
                type="primary",
                use_container_width=True,
            )

        if submit_button:
            if st.session_state["quiz2_attempts"] >= MAX_ATTEMPTS:
                st.error("❌ You have reached the maximum number of attempts for this quiz.")
                return

            if None in st.session_state["user_answers_quiz2"]:
                st.error("❌ Please answer all questions before submitting.")
                return

            score = sum(
                question["points"]
                for i, question in enumerate(questions)
                if st.session_state["user_answers_quiz2"][i] == question["answer"]
            )

            st.session_state["quiz2_attempts"] += 1
            
            # Display results
            st.markdown("### Quiz Results")
            st.progress(score/100)
            st.success(f"📊 Your score: {score}/100")

            # Update database
            db_path = st.secrets["general"]["db_path"]
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE records SET quiz2 = ? WHERE username = ?",
                              (score, st.session_state["verified_username"]))
                conn.commit()
                
                if cursor.rowcount == 0:
                    st.error("Grade update failed: No matching username found.")
                else:
                    st.success("Grade successfully saved.")
                    push_db_to_github(db_path)  # Optional GitHub sync
                
                conn.close()
            except Exception as e:
                st.error(f"Error saving grade: {e}")

if __name__ == "__main__":
    show()
