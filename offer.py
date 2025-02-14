import streamlit as st

def show():
    st.title("AI for Impact")
    st.subheader("What We Offer")

    # Create tabs for each course
    tabs = st.tabs(["Course 1", "Course 2"])

    # ──────────────────────────────
    # Course 1 Tab
    with tabs[0]:
        st.header("Course 1: Foundations of Python Programming and Applied Coding")
        st.write(
            "Impact: Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, "
            "and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications."
        )
        st.markdown("**Course Chapters:**")
        st.write("- Week 1: Introduction to Coding")
        st.write("- Week 2: Generate Comprehensive Codings")
        st.write("- Week 3: Deploy Apps with GitHub and Streamlit")
        st.write("- Week 4: Data Week")
        st.write("📌 Availability: ✅ Included in Basic, Pro, and VIP Plans")

        if st.button("Start", key="start_course1"):
            # Set query parameter to indicate navigation to login page
            st.experimental_set_query_params(page="login")
            st.experimental_rerun()

    # ──────────────────────────────
    # Course 2 Tab
    with tabs[1]:
        st.header("Course 2: Advanced Machine Learning and Real-Time Deployment")
        st.write(
            "Impact: Participants will develop advanced skills in database management, machine learning, and real-time application deployment. "
            "This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, "
            "and integrate apps with cloud and database systems."
        )
        st.markdown("**Course Chapters:**")
        st.write("- Week 1: Advanced SQL and Databases")
        st.write("- Week 2: Deploy Database")
        st.write("- Week 3: Unsupervised Machine Learning")
        st.write("- Week 4: Supervised Machine Learning")
        st.write("- Week 5: Processing Data in Real-Time for Decision-Making")
        st.write("- Week 6: Capstone Project")
        st.write("📌 Availability: ✅ Included in Pro and VIP Plans (Not available in Basic Plan)")

        if st.button("Start", key="start_course2"):
            # Set query parameter to indicate navigation to loginx page
            st.experimental_set_query_params(page="loginx")
            st.experimental_rerun()

if __name__ == '__main__':
    show()
