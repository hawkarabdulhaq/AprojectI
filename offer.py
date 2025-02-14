import streamlit as st

def show_offer():
    st.title("AI for Impact")
    st.subheader("What We Offer")

    tabs = st.tabs([
        "Course 1: Foundations of Python Programming and Applied Coding",
        "Course 2: Advanced Machine Learning and Real-Time Deployment"
    ])

    with tabs[0]:
        st.markdown("### Course 1: Foundations of Python Programming and Applied Coding")
        st.markdown(
            "**Impact:** Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications."
        )
        st.markdown("**Course Chapters:**")
        st.markdown("- Week 1: Introduction to Coding")
        st.markdown("- Week 2: Generate Comprehensive Codings")
        st.markdown("- Week 3: Deploy Apps with GitHub and Streamlit")
        st.markdown("- Week 4: Data Week")
        st.markdown("📌 **Availability:** ✅ Included in Basic, Pro, and VIP Plans")
        if st.button("Start", key="start_course1"):
            st.session_state["course"] = "course1"

    with tabs[1]:
        st.markdown("### Course 2: Advanced Machine Learning and Real-Time Deployment")
        st.markdown(
            "**Impact:** Participants will develop advanced skills in database management, machine learning, and real-time application deployment. This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems."
        )
        st.markdown("**Course Chapters:**")
        st.markdown("- Week 1: Advanced SQL and Databases")
        st.markdown("- Week 2: Deploy Database")
        st.markdown("- Week 3: Unsupervised Machine Learning")
        st.markdown("- Week 4: Supervised Machine Learning")
        st.markdown("- Week 5: Processing Data in Real-Time for Decision-Making")
        st.markdown("- Week 6: Capstone Project")
        st.markdown("📌 **Availability:** ✅ Included in Pro and VIP Plans (Not available in Basic Plan)")
        if st.button("Start", key="start_course2"):
            st.session_state["course"] = "course2"

    # If a course was selected, rerun the app to load the next page.
    if "course" in st.session_state:
        st.experimental_rerun()

if __name__ == "__main__":
    show_offer()
