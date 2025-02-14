import streamlit as st

def create_programming_svg():
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="150" height="150" style="float: right; margin-left: 20px;">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#4CAF50;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#81C784;stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect x="20" y="20" width="160" height="160" fill="url(#grad1)" rx="20"/>
        <circle cx="140" cy="60" r="15" fill="white" opacity="0.3"/>
        <text x="100" y="90" font-family="Arial" font-size="30" fill="white" text-anchor="middle">&lt;/&gt;</text>
        <text x="100" y="130" font-family="Arial" font-size="16" fill="white" text-anchor="middle">Python</text>
        <path d="M40,100 L80,60 L120,100 L160,60" stroke="white" stroke-width="4" fill="none" opacity="0.5"/>
    </svg>
    '''

def create_ml_svg():
    return '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="150" height="150" style="float: right; margin-left: 20px;">
        <defs>
            <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#2196F3;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#64B5F6;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="100" cy="100" r="90" fill="url(#grad2)"/>
        <circle cx="70" cy="70" r="10" fill="white"/>
        <circle cx="130" cy="70" r="10" fill="white"/>
        <circle cx="100" cy="130" r="10" fill="white"/>
        <circle cx="70" cy="160" r="10" fill="white"/>
        <circle cx="130" cy="160" r="10" fill="white"/>
        <path d="M70,70 L130,70 L100,130 L70,160 L130,160" stroke="white" stroke-width="4" fill="none"/>
        <text x="100" y="100" font-family="Arial" font-size="16" fill="white" text-anchor="middle">ML</text>
    </svg>
    '''

def show():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .title-container {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #1E88E5 0%, #64B5F6 100%);
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .title-text {
            color: white;
            font-size: 3em;
            font-weight: bold;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .header-text {
            color: white;
            font-size: 1.8em;
            margin-top: 1rem;
        }
        .course-container {
            display: flex;
            align-items: start;
            margin: 2rem 0;
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .course-content {
            flex: 1;
        }
        .subheader-text {
            color: #2196F3;
            font-size: 1.8em;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #2196F3;
            padding-bottom: 0.5rem;
        }
        .impact-text {
            color: #4CAF50;
            font-weight: bold;
            font-size: 1.2em;
            margin: 1.5rem 0;
        }
        .chapter-container {
            background: #f5f5f5;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        .chapter-title {
            color: #424242;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .chapter-list {
            color: #666666;
            margin-left: 1.5rem;
        }
        .availability-text {
            color: #FF5722;
            font-weight: bold;
            margin-top: 1.5rem;
            padding: 1rem;
            background: #FBE9E7;
            border-radius: 8px;
        }
        .stButton button {
            background: #2196F3;
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 25px;
            border: none;
            font-weight: bold;
            margin-top: 1rem;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: #1976D2;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        div[data-testid="stVerticalBlock"] {
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown('''
        <div class="title-container">
            <p class="title-text">AI for Impact</p>
            <p class="header-text">What We Offer</p>
        </div>
    ''', unsafe_allow_html=True)

    # Center-align the tabs container
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    tabs = st.tabs([
        "Course 1: Foundations of Python Programming",
        "Course 2: Advanced Machine Learning"
    ])
    st.markdown('</div>', unsafe_allow_html=True)

    # Course 1 Tab
    with tabs[0]:
        st.markdown('''
            <div class="course-container">
                <div class="course-content">
                    <h2 class="subheader-text">Foundations of Python Programming</h2>
                    
                    <p class="impact-text">Impact:</p>
                    <p>Participants will gain foundational skills in Python programming and learn to create robust scripts, 
                    work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, 
                    process data, and build basic web applications.</p>
                    
                    <div class="chapter-container">
                        <p class="chapter-title">Course Chapters:</p>
                        <ul class="chapter-list">
                            <li>Week 1: Introduction to Coding</li>
                            <li>Week 2: Generate Comprehensive Codings</li>
                            <li>Week 3: Deploy Apps with GitHub and Streamlit</li>
                            <li>Week 4: Data Week</li>
                        </ul>
                    </div>
                    
                    <p class="availability-text">📌 Availability: ✅ Included in Basic, Pro, and VIP Plans</p>
                </div>
                ''' + create_programming_svg() + '''
            </div>
        ''', unsafe_allow_html=True)
        
        if st.button("Start Course 1"):
            st.session_state["page"] = "login"
            st.rerun()

    # Course 2 Tab
    with tabs[1]:
        st.markdown('''
            <div class="course-container">
                <div class="course-content">
                    <h2 class="subheader-text">Advanced Machine Learning</h2>
                    
                    <p class="impact-text">Impact:</p>
                    <p>Participants will develop advanced skills in database management, machine learning, and real-time 
                    application deployment. This course focuses on practical implementations, enabling learners to create 
                    AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems.</p>
                    
                    <div class="chapter-container">
                        <p class="chapter-title">Course Chapters:</p>
                        <ul class="chapter-list">
                            <li>Week 1: Advanced SQL and Databases</li>
                            <li>Week 2: Deploy Database</li>
                            <li>Week 3: Unsupervised Machine Learning</li>
                            <li>Week 4: Supervised Machine Learning</li>
                            <li>Week 5: Processing Data in Real-Time for Decision-Making</li>
                            <li>Week 6: Capstone Project</li>
                        </ul>
                    </div>
                    
                    <p class="availability-text">📌 Availability: ✅ Included in Pro and VIP Plans (Not available in Basic Plan)</p>
                </div>
                ''' + create_ml_svg() + '''
            </div>
        ''', unsafe_allow_html=True)
        
        if st.button("Start Course 2"):
            st.session_state["page"] = "loginx"
            st.rerun()
