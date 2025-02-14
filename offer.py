import streamlit as st

def create_programming_svg():
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="50" height="50">
        <rect x="10" y="10" width="80" height="80" fill="#4CAF50" rx="10"/>
        <text x="50" y="50" font-family="Arial" font-size="40" fill="white" text-anchor="middle" dominant-baseline="middle">&lt;/&gt;</text>
        <circle cx="70" cy="30" r="8" fill="#81C784"/>
    </svg>
    '''

def create_ml_svg():
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="50" height="50">
        <circle cx="50" cy="50" r="45" fill="#2196F3"/>
        <path d="M30,50 L45,65 L75,35" stroke="white" stroke-width="8" fill="none"/>
        <circle cx="30" cy="50" r="5" fill="white"/>
        <circle cx="45" cy="65" r="5" fill="white"/>
        <circle cx="75" cy="35" r="5" fill="white"/>
    </svg>
    '''

def show():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .title-text {
            color: #1E88E5;
            font-size: 2.5em;
            font-weight: bold;
        }
        .header-text {
            color: #424242;
            font-size: 1.8em;
        }
        .subheader-text {
            color: #2196F3;
            font-size: 1.5em;
        }
        .impact-text {
            color: #4CAF50;
            font-weight: bold;
        }
        .chapter-text {
            color: #666666;
        }
        .availability-text {
            color: #FF5722;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="title-text">AI for Impact</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-text">What We Offer</p>', unsafe_allow_html=True)

    tabs = st.tabs([
        "Course 1: Foundations of Python Programming and Applied Coding",
        "Course 2: Advanced Machine Learning and Real-Time Deployment"
    ])

    # Course 1 Tab
    with tabs[0]:
        st.markdown(create_programming_svg(), unsafe_allow_html=True)
        st.markdown('<p class="subheader-text">Course 1: Foundations of Python Programming and Applied Coding</p>', unsafe_allow_html=True)
        st.markdown("""
        <p class="impact-text">Impact:</p> Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications.

        <p class="chapter-text">**Course Chapters:**
        - Week 1: Introduction to Coding
        - Week 2: Generate Comprehensive Codings
        - Week 3: Deploy Apps with GitHub and Streamlit
        - Week 4: Data Week</p>

        <p class="availability-text">📌 **Availability:** ✅ Included in Basic, Pro, and VIP Plans</p>
        """, unsafe_allow_html=True)
        
        if st.button("Start Course 1"):
            st.session_state["page"] = "login"
            st.rerun()

    # Course 2 Tab
    with tabs[1]:
        st.markdown(create_ml_svg(), unsafe_allow_html=True)
        st.markdown('<p class="subheader-text">Course 2: Advanced Machine Learning and Real-Time Deployment</p>', unsafe_allow_html=True)
        st.markdown("""
        <p class="impact-text">Impact:</p> Participants will develop advanced skills in database management, machine learning, and real-time application deployment. This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems.

        <p class="chapter-text">**Course Chapters:**
        - Week 1: Advanced SQL and Databases
        - Week 2: Deploy Database
        - Week 3: Unsupervised Machine Learning
        - Week 4: Supervised Machine Learning
        - Week 5: Processing Data in Real-Time for Decision-Making
        - Week 6: Capstone Project</p>

        <p class="availability-text">📌 **Availability:** ✅ Included in Pro and VIP Plans (Not available in Basic Plan)</p>
        """, unsafe_allow_html=True)
        
        if st.button("Start Course 2"):
            st.session_state["page"] = "loginx"
            st.rerun()
