import streamlit as st

def show_offer():
    st.title("AI for Impact")
    st.subheader("What We Offer")

    # Create tabs for the two courses
    course_tabs = st.tabs([
        "Course 1: Foundations of Python Programming and Applied Coding",
        "Course 2: Advanced Machine Learning and Real-Time Deployment"
    ])

    # ──────────────── Course 1 Tab ────────────────
    with course_tabs[0]:
        st.header("Course 1: Foundations of Python Programming and Applied Coding")
        st.markdown(
            """
            **Impact:** Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications.
            
            **Course Chapters:**
            - **Week 1:** Introduction to Coding
            - **Week 2:** Generate Comprehensive Codings
            - **Week 3:** Deploy Apps with GitHub and Streamlit
            - **Week 4:** Data Week
            
            📌 **Availability:** ✅ Included in Basic, Pro, and VIP Plans
            """
        )
        if st.button("Start", key="start_course1"):
            # Import and show the login page from login.py
            import login
            login.show_login_create_account()

    # ──────────────── Course 2 Tab ────────────────
    with course_tabs[1]:
        st.header("Course 2: Advanced Machine Learning and Real-Time Deployment")
        st.markdown(
            """
            **Impact:** Participants will develop advanced skills in database management, machine learning, and real-time application deployment. This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems.
            
            **Course Chapters:**
            - **Week 1:** Advanced SQL and Databases
            - **Week 2:** Deploy Database
            - **Week 3:** Unsupervised Machine Learning
            - **Week 4:** Supervised Machine Learning
            - **Week 5:** Processing Data in Real-Time for Decision-Making
            - **Week 6:** Capstone Project
            
            📌 **Availability:** ✅ Included in Pro and VIP Plans (Not available in Basic Plan)
            """
        )
        if st.button("Start", key="start_course2"):
            # Import and show the login page from loginx.py
            import loginx
            loginx.show_login_create_account()

if __name__ == "__main__":
    show_offer()
