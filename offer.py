import streamlit as st

def show_offer():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .big-title {
            font-size: 3.5rem !important;
            color: #FFB366 !important;
            text-align: center !important;
            padding: 2rem 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            background: linear-gradient(45deg, #FFB366, #FFD6B3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
        }
        .week-highlight {
            color: #2E86C1;
            font-weight: 600;
        }
        .impact-section {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        .availability {
            background-color: #e8f4f9;
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1rem;
        }
        .start-button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 2rem;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main title with custom styling
    st.markdown('<h1 class="big-title">AI for Impact</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #666;">What We Offer</h2>', unsafe_allow_html=True)

    # Create tabs with custom styling
    course_tabs = st.tabs([
        "🔰 Course 1: Foundations of Python Programming",
        "🚀 Course 2: Advanced Machine Learning"
    ])

    # Course 1 Tab
    with course_tabs[0]:
        st.header("Course 1: Foundations of Python Programming and Applied Coding")
        
        st.markdown("""
        <div class="impact-section">
        <h3>💫 Impact</h3>
        Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, 
        and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, 
        and build basic web applications.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### 📚 Course Chapters:
        - <span class="week-highlight">Week 1:</span> Introduction to Coding
        - <span class="week-highlight">Week 2:</span> Generate Comprehensive Codings
        - <span class="week-highlight">Week 3:</span> Deploy Apps with GitHub and Streamlit
        - <span class="week-highlight">Week 4:</span> Data Week
        
        <div class="availability">
        📌 <strong>Availability:</strong> ✅ Included in Basic, Pro, and VIP Plans
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Now", key="start_course1", help="Begin your Python journey"):
            import login
            login.show_login_create_account()

    # Course 2 Tab
    with course_tabs[1]:
        st.header("Course 2: Advanced Machine Learning and Real-Time Deployment")
        
        st.markdown("""
        <div class="impact-section">
        <h3>💫 Impact</h3>
        Participants will develop advanced skills in database management, machine learning, and real-time application deployment. 
        This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in 
        real-world scenarios, and integrate apps with cloud and database systems.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### 📚 Course Chapters:
        - <span class="week-highlight">Week 1:</span> Advanced SQL and Databases
        - <span class="week-highlight">Week 2:</span> Deploy Database
        - <span class="week-highlight">Week 3:</span> Unsupervised Machine Learning
        - <span class="week-highlight">Week 4:</span> Supervised Machine Learning
        - <span class="week-highlight">Week 5:</span> Processing Data in Real-Time for Decision-Making
        - <span class="week-highlight">Week 6:</span> Capstone Project
        
        <div class="availability">
        📌 <strong>Availability:</strong> ✅ Included in Pro and VIP Plans (Not available in Basic Plan)
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Now", key="start_course2", help="Begin your ML journey"):
            import loginx
            loginx.show_login_create_account()

if __name__ == "__main__":
    show_offer()
