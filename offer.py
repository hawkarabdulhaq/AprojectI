import streamlit as st

def create_programming_svg():
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="120" height="120" style="float: right; margin-top: -60px;">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#4CAF50;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#81C784;stop-opacity:1" />
            </linearGradient>
            <filter id="shadow1">
                <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
            </filter>
        </defs>
        <rect x="20" y="20" width="160" height="160" fill="url(#grad1)" rx="20" filter="url(#shadow1)"/>
        <text x="100" y="90" font-family="Arial" font-size="30" fill="white" text-anchor="middle">&lt;/&gt;</text>
        <text x="100" y="130" font-family="Arial" font-size="16" fill="white" text-anchor="middle">Python</text>
        <circle cx="140" cy="60" r="15" fill="#81C784"/>
        <path d="M45,40 L75,40 M45,60 L85,60 M45,80 L65,80" stroke="white" stroke-width="6"/>
    </svg>
    '''

def create_ml_svg():
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="120" height="120" style="float: right; margin-top: -60px;">
        <defs>
            <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#2196F3;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#64B5F6;stop-opacity:1" />
            </linearGradient>
            <filter id="shadow2">
                <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
            </filter>
        </defs>
        <circle cx="100" cy="100" r="90" fill="url(#grad2)" filter="url(#shadow2)"/>
        <g fill="none" stroke="white" stroke-width="4">
            <circle cx="70" cy="70" r="20"/>
            <circle cx="130" cy="70" r="20"/>
            <circle cx="100" cy="130" r="20"/>
        </g>
        <path d="M70,70 L130,70 L100,130 L70,70" stroke="white" stroke-width="4" fill="none"/>
        <text x="100" y="160" font-family="Arial" font-size="16" fill="white" text-anchor="middle">ML & AI</text>
    </svg>
    '''

def show():
    # Custom CSS for styling with animations and enhanced design
    st.markdown("""
        <style>
        @keyframes shine {
            0% { text-shadow: 0 0 5px rgba(30,136,229,0); }
            50% { text-shadow: 0 0 20px rgba(30,136,229,0.5); }
            100% { text-shadow: 0 0 5px rgba(30,136,229,0); }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .title-container {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .title-text {
            color: #1E88E5;
            font-size: 3.5em;
            font-weight: bold;
            animation: shine 3s infinite;
            text-align: center;
            margin-bottom: 1rem;
            background: linear-gradient(45deg, #1E88E5, #64B5F6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .header-text {
            color: #424242;
            font-size: 2.2em;
            text-align: center;
            margin-bottom: 2rem;
            animation: fadeIn 1s ease-out;
        }
        
        .subheader-text {
            color: #2196F3;
            font-size: 2em;
            font-weight: bold;
            margin: 1.5rem 0;
            animation: fadeIn 1s ease-out;
        }
        
        .impact-text {
            color: #4CAF50;
            font-weight: bold;
            font-size: 1.3em;
            margin-top: 1rem;
            animation: fadeIn 1.2s ease-out;
        }
        
        .chapter-text {
            color: #666666;
            font-size: 1.1em;
            line-height: 1.6;
            margin: 1rem 0;
            animation: fadeIn 1.4s ease-out;
        }
        
        .availability-text {
            color: #FF5722;
            font-weight: bold;
            font-size: 1.2em;
            margin-top: 1.5rem;
            padding: 1rem;
            border-radius: 8px;
            background: rgba(255,87,34,0.1);
            animation: fadeIn 1.6s ease-out;
        }
        
        /* Center tab labels */
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
            gap: 2rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 1rem 2rem;
            font-size: 1.1em;
            background: #f5f5f5;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: #e0e0e0;
        }
        
        /* Style for the buttons */
        .stButton button {
            width: 200px;
            height: 50px;
            font-size: 1.2em;
            font-weight: bold;
            border-radius: 25px;
            transition: all 0.3s ease;
            margin: 2rem auto;
            display: block;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .course-content {
            padding: 2rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-top: 2rem;
            animation: fadeIn 1s ease-out;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown('<div class="title-container">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">AI for Impact</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-text">What We Offer</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    tabs = st.tabs([
        "Course 1: Foundations of Python Programming",
        "Course 2: Advanced Machine Learning"
    ])

    # Course 1 Tab
    with tabs[0]:
        st.markdown('<div class="course-content">', unsafe_allow_html=True)
        st.markdown(create_programming_svg(), unsafe_allow_html=True)
        st.markdown('<p class="subheader-text">Foundations of Python Programming and Applied Coding</p>', unsafe_allow_html=True)
        st.markdown("""
        <p class="impact-text">🚀 Impact</p>
        <p>Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications.</p>

        <p class="chapter-text">📚 <strong>Course Chapters:</strong>
        <br>• Week 1: Introduction to Coding - Fundamentals & Best Practices
        <br>• Week 2: Generate Comprehensive Codings - Advanced Techniques
        <br>• Week 3: Deploy Apps with GitHub and Streamlit - Real-world Applications
        <br>• Week 4: Data Week - Working with Data Structures & Analytics</p>

        <p class="availability-text">📌 <strong>Availability:</strong> ✅ Included in Basic, Pro, and VIP Plans</p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("Start Course 1"):
            st.session_state["page"] = "login"
            st.rerun()

    # Course 2 Tab
    with tabs[1]:
        st.markdown('<div class="course-content">', unsafe_allow_html=True)
        st.markdown(create_ml_svg(), unsafe_allow_html=True)
        st.markdown('<p class="subheader-text">Advanced Machine Learning and Real-Time Deployment</p>', unsafe_allow_html=True)
        st.markdown("""
        <p class="impact-text">🚀 Impact</p>
        <p>Participants will develop advanced skills in database management, machine learning, and real-time application deployment. This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems.</p>

        <p class="chapter-text">📚 <strong>Course Chapters:</strong>
        <br>• Week 1: Advanced SQL and Databases - Modern Database Architecture
        <br>• Week 2: Deploy Database - Cloud Integration & Scaling
        <br>• Week 3: Unsupervised Machine Learning - Clustering & Dimensionality Reduction
        <br>• Week 4: Supervised Machine Learning - Classification & Regression
        <br>• Week 5: Processing Data in Real-Time - Stream Processing & Decision Systems
        <br>• Week 6: Capstone Project - End-to-End ML Solution</p>

        <p class="availability-text">📌 <strong>Availability:</strong> ✅ Included in Pro and VIP Plans (Not available in Basic Plan)</p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("Start Course 2"):
            st.session_state["page"] = "loginx"
            st.rerun()
