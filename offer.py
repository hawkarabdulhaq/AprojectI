import streamlit as st

# Custom CSS to style the titles, tabs, and layout
st.markdown("""
    <style>
        .big-font {
            font-size: 40px !important;
            font-weight: bold !important;
            text-align: center !important;
            color: #4A90E2 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        .header-font {
            font-size: 30px !important;
            font-weight: bold !important;
            text-align: center !important;
            color: #4A90E2 !important;
        }
        .subheader-font {
            font-size: 24px !important;
            font-weight: bold !important;
            color: #4A90E2 !important;
        }
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 18px !important;
            font-weight: bold !important;
            color: #4A90E2 !important;
        }
        .stButton button {
            background-color: #4A90E2 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
        }
        .stButton button:hover {
            background-color: #357ABD !important;
        }
        .svg-container {
            float: right;
            margin-left: 20px;
            margin-top: -50px;
        }
    </style>
""", unsafe_allow_html=True)

def show():
    # Main title with custom styling
    st.markdown('<p class="big-font">AI for Impact</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-font">What We Offer</p>', unsafe_allow_html=True)

    # Tabs for courses
    tabs = st.tabs([
        "Course 1: Foundations of Python Programming and Applied Coding",
        "Course 2: Advanced Machine Learning and Real-Time Deployment"
    ])

    # Course 1 Tab
    with tabs[0]:
        st.markdown('<p class="subheader-font">Course 1: Foundations of Python Programming and Applied Coding</p>', unsafe_allow_html=True)
        
        # Placeholder for SVG image (replace with actual SVG file path)
        st.markdown('<div class="svg-container"><img src="https://via.placeholder.com/150" alt="Course 1 SVG"></div>', unsafe_allow_html=True)
        
        st.markdown("""\
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
            st.rerun()

    # Course 2 Tab
    with tabs[1]:
        st.markdown('<p class="subheader-font">Course 2: Advanced Machine Learning and Real-Time Deployment</p>', unsafe_allow_html=True)
        
        # Placeholder for SVG image (replace with actual SVG file path)
        st.markdown('<div class="svg-container"><img src="https://via.placeholder.com/150" alt="Course 2 SVG"></div>', unsafe_allow_html=True)
        
        st.markdown("""\
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
            st.rerun()

# Run the show function
show()
