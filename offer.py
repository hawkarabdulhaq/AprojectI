import streamlit as st

def show():
    st.title("AI for Impact")
    st.header("What We Offer")

    tabs = st.tabs([
        "Course 1: Foundations of Python Programming and Applied Coding",
        "Course 2: Advanced Machine Learning and Real-Time Deployment"
    ])

    # Tab for Course 1
    with tabs[0]:
        st.subheader("Course 1: Foundations of Python Programming and Applied Coding")
        st.markdown("""
Impact: Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications.

**Course Chapters:**
- Week 1: Introduction to Coding
- Week 2: Generate Comprehensive Codings
- Week 3: Deploy Apps with GitHub and Streamlit
- Week 4: Data Week

📌 **Availability:** ✅ Included in Basic, Pro, and VIP Plans
        """)
        if st.button("Start Course 1"):
            st.session_state["page"] = "login"
            st.experimental_rerun()

    # Tab for Course 2
    with tabs[1]:
        st.subheader("Course 2: Advanced Machine Learning and Real-Time Deployment")
        st.markdown("""
Impact: Participants will develop advanced skills in database management, machine learning, and real-time application deployment. This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems.

**Course Chapters:**
- Week 1: Advanced SQL and Databases
- Week 2: Deploy Database
- Week 3: Unsupervised Machine Learning
- Week 4: Supervised Machine Learning
- Week 5: Processing Data in Real-Time for Decision-Making
- Week 6: Capstone Project

📌 **Availability:** ✅ Included in Pro and VIP Plans (Not available in Basic Plan)
        """)
        if st.button("Start Course 2"):
            st.session_state["page"] = "loginx"
            st.experimental_rerun()
