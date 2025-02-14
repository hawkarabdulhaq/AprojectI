import streamlit as st
from datetime import datetime
import pytz

def create_programming_svg():
    # Your existing SVG code remains the same
    pass

def create_ml_svg():
    # Your existing SVG code remains the same
    pass

def show():
    # Get current UTC time
    current_utc = datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
    
    st.markdown("""
        <style>
        /* Your existing styles remain the same */
        
        /* Add styles for the header info */
        .header-info {
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            padding: 1rem;
            border-radius: 10px;
            color: #F8FAFC;
            margin-bottom: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .header-label {
            color: #94A3B8;
            font-size: 0.9rem;
        }
        
        .header-value {
            color: #F8FAFC;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    # Add header info section
    st.markdown(f'''
        <div class="header-info">
            <div class="header-item">
                <span class="header-label">UTC:</span>
                <span class="header-value">{current_utc}</span>
            </div>
            <div class="header-item">
                <span class="header-label">User:</span>
                <span class="header-value">Hakari-Bibani</span>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    # Main Content
    st.markdown('''
        <div class="hero-section">
            <h1 class="hero-title">AI for Impact</h1>
            <h2 class="hero-subtitle">What We Offer</h2>
        </div>
    ''', unsafe_allow_html=True)

    tabs = st.tabs([
        "Course 1: Foundations of Python Programming",
        "Course 2: Advanced Machine Learning"
    ])

    # Course 1
    with tabs[0]:
        st.markdown(f'''
            <div class="course-card">
                {create_programming_svg()}
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
        
        if st.button("Start Course 1", key="btn1"):
            st.session_state["page"] = "login"
            st.rerun()

    # Course 2
    with tabs[1]:
        st.markdown(f'''
            <div class="course-card">
                {create_ml_svg()}
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
        
        if st.button("Start Course 2", key="btn2"):
            st.session_state["page"] = "loginx"
            st.rerun()
