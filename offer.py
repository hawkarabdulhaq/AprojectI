import streamlit as st

def show():
    st.markdown("""
        <style>
        /* Layout */
        .main-container {
            display: flex;
            gap: 2rem;
            padding: 2rem;
            min-height: 100vh;
        }
        
        .content-area {
            flex: 1;
            padding: 2rem;
        }
        
        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            padding: 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .hero-title {
            font-size: 3rem;
            color: #F8FAFC;
            margin-bottom: 1rem;
            font-weight: 800;
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            color: #94A3B8;
        }
        
        /* Side Banner */
        .side-banner {
            width: 300px;
            background: #F8FAFC;
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            height: fit-content;
            position: sticky;
            top: 2rem;
        }
        
        .banner-item {
            padding: 1rem;
            margin: 0.5rem 0;
            background: white;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .banner-item:hover {
            transform: translateX(5px);
            background: #F1F5F9;
        }
        
        .banner-item.active {
            border-color: #3B82F6;
            background: #EFF6FF;
        }
        
        .banner-title {
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 0.5rem;
        }
        
        /* Course Content */
        .course-content {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            animation: slideIn 0.5s ease-out;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .course-title {
            font-size: 2.2rem;
            color: #1E293B;
            margin-bottom: 1.5rem;
        }
        
        .impact-section {
            background: #F8FAFC;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1.5rem 0;
        }
        
        .impact-title {
            color: #0F172A;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        .impact-text {
            color: #475569;
            line-height: 1.6;
        }
        
        .chapter-item {
            padding: 1rem;
            margin: 0.5rem 0;
            background: #F8FAFC;
            border-radius: 10px;
            color: #475569;
            transition: all 0.3s ease;
        }
        
        .chapter-item:hover {
            background: #F1F5F9;
            transform: translateX(10px);
        }
        
        .availability-badge {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
            color: white;
            border-radius: 50px;
            font-weight: 600;
            margin-top: 1.5rem;
        }
        
        .start-button {
            display: inline-block;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #3A416F 0%, #141727 100%);
            color: white;
            border-radius: 50px;
            font-weight: 600;
            margin-top: 2rem;
            cursor: pointer;
            border: none;
            width: 100%;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state for selected course
    if 'selected_course' not in st.session_state:
        st.session_state.selected_course = "python"

    # Main container
    st.markdown('''
        <div class="hero-section">
            <h1 class="hero-title">AI for Impact</h1>
            <h2 class="hero-subtitle">What We Offer</h2>
        </div>
        
        <div class="main-container">
            <div class="content-area">
    ''', unsafe_allow_html=True)

    # Course content based on selection
    if st.session_state.selected_course == "python":
        st.markdown('''
            <div class="course-content">
                <h2 class="course-title">Foundations of Python Programming and Applied Coding</h2>
                
                <div class="impact-section">
                    <h3 class="impact-title">🎯 Impact</h3>
                    <p class="impact-text">Participants will gain foundational skills in Python programming and learn to create robust scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate tasks, process data, and build basic web applications.</p>
                </div>

                <div class="chapters-section">
                    <h3 class="impact-title">📚 Course Chapters</h3>
                    <div class="chapter-item">Week 1: Introduction to Coding</div>
                    <div class="chapter-item">Week 2: Generate Comprehensive Codings</div>
                    <div class="chapter-item">Week 3: Deploy Apps with GitHub and Streamlit</div>
                    <div class="chapter-item">Week 4: Data Week</div>
                </div>

                <div class="availability-badge">
                    ✅ Included in Basic, Pro, and VIP Plans
                </div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button("Start Course 1"):
            st.session_state["page"] = "login"
            st.rerun()
    else:
        st.markdown('''
            <div class="course-content">
                <h2 class="course-title">Advanced Machine Learning and Real-Time Deployment</h2>
                
                <div class="impact-section">
                    <h3 class="impact-title">🎯 Impact</h3>
                    <p class="impact-text">Participants will develop advanced skills in database management, machine learning, and real-time application deployment. This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems.</p>
                </div>

                <div class="chapters-section">
                    <h3 class="impact-title">📚 Course Chapters</h3>
                    <div class="chapter-item">Week 1: Advanced SQL and Databases</div>
                    <div class="chapter-item">Week 2: Deploy Database</div>
                    <div class="chapter-item">Week 3: Unsupervised Machine Learning</div>
                    <div class="chapter-item">Week 4: Supervised Machine Learning</div>
                    <div class="chapter-item">Week 5: Processing Data in Real-Time for Decision-Making</div>
                    <div class="chapter-item">Week 6: Capstone Project</div>
                </div>

                <div class="availability-badge">
                    ✅ Included in Pro and VIP Plans (Not available in Basic Plan)
                </div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button("Start Course 2"):
            st.session_state["page"] = "loginx"
            st.rerun()

    # Side Banner
    st.sidebar.markdown('''
        <div class="side-banner">
            <div class="banner-item {}" onclick="handleClick('python')">
                <div class="banner-title">Python Programming</div>
                <small>Foundations & Applied Coding</small>
            </div>
            <div class="banner-item {}" onclick="handleClick('ml')">
                <div class="banner-title">Machine Learning</div>
                <small>Advanced & Real-Time Deployment</small>
            </div>
        </div>
    '''.format(
        'active' if st.session_state.selected_course == "python" else '',
        'active' if st.session_state.selected_course == "ml" else ''
    ), unsafe_allow_html=True)

    # JavaScript for handling clicks
    st.markdown('''
        <script>
        function handleClick(course) {
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: course
            }, '*');
        }
        </script>
    ''', unsafe_allow_html=True)

    # Handle sidebar selection
    if st.sidebar.button("Python Programming", key="python_btn"):
        st.session_state.selected_course = "python"
        st.rerun()
    if st.sidebar.button("Machine Learning", key="ml_btn"):
        st.session_state.selected_course = "ml"
        st.rerun()
