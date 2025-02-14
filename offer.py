import streamlit as st
from streamlit.components.v1 import html

# Custom CSS with modern styling and animations
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        .main-title {
            font-size: 2.8rem !important;
            font-weight: 700 !important;
            text-align: center;
            background: linear-gradient(45deg, #4F46E5, #EC4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 1.5rem 0;
            text-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .header {
            font-size: 2rem !important;
            text-align: center;
            color: #374151 !important;
            margin-bottom: 2rem !important;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: #f8f9fa !important;
            border-radius: 12px !important;
            padding: 1rem 2rem !important;
            transition: all 0.3s ease !important;
            border: 2px solid #e5e7eb !important;
            font-weight: 600 !important;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stTabs [aria-selected="true"] {
            background: #4F46E5 !important;
            color: white !important;
            border-color: #4F46E5 !important;
        }
        
        .course-card {
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border: 1px solid #e5e7eb;
        }
        
        .svg-container {
            float: right;
            margin: 0 0 1rem 2rem;
            width: 220px;
            height: 220px;
            border-radius: 12px;
            overflow: hidden;
            background: #f8f9fa;
        }
        
        .stButton button {
            background: linear-gradient(45deg, #4F46E5, #6366F1) !important;
            color: white !important;
            border: none !important;
            padding: 0.8rem 2rem !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(79,70,229,0.3);
        }
        
        .availability-tag {
            display: inline-block;
            background: #e0e7ff;
            color: #4F46E5;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            margin: 1rem 0;
        }
        
        .course-chapters {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

def show():
    # Main title with gradient effect
    st.markdown('<h1 class="main-title">🚀 AI for Impact</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="header">What We Offer</h2>', unsafe_allow_html=True)

    tabs = st.tabs([
        "🌟 Foundations of Python", 
        "🚀 Advanced ML & Deployment"
    ])

    with tabs[0]:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown("""
                    <div class="course-card">
                        <h3 style="font-size:1.6rem; color:#1f2937; margin-bottom:1rem;">
                            Foundations of Python Programming
                        </h3>
                        <div class="availability-tag">✅ Basic, Pro & VIP Plans</div>
                        <p style="color:#4b5563; line-height:1.6;">
                            Master Python fundamentals and build practical applications through hands-on projects. 
                            Learn to automate workflows, process data, and deploy web applications.
                        </p>
                        <div class="course-chapters">
                            <h4 style="margin:0 0 1rem 0; color:#4F46E5;">Course Structure:</h4>
                            <ul style="list-style-type: none; padding-left: 0; margin: 0;">
                                <li>📌 Week 1: Python Essentials</li>
                                <li>📌 Week 2: API Integration</li>
                                <li>📌 Week 3: GitHub & Deployment</li>
                                <li>📌 Week 4: Data Analysis</li>
                            </ul>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Start Course 1 →", key="course1"):
                    st.session_state["page"] = "login"
                    st.rerun()
            
            with col2:
                st.markdown("""
                    <div class="svg-container">
                        <img src="https://www.svgrepo.com/show/376344/python.svg" 
                             style="width:100%; height:100%; object-fit:cover;">
                    </div>
                """, unsafe_allow_html=True)

    with tabs[1]:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown("""
                    <div class="course-card">
                        <h3 style="font-size:1.6rem; color:#1f2937; margin-bottom:1rem;">
                            Advanced Machine Learning & Deployment
                        </h3>
                        <div class="availability-tag">✅ Pro & VIP Plans Only</div>
                        <p style="color:#4b5563; line-height:1.6;">
                            Dive deep into ML algorithms, real-time deployment, and cloud integration. 
                            Build production-ready AI solutions with end-to-end project experience.
                        </p>
                        <div class="course-chapters">
                            <h4 style="margin:0 0 1rem 0; color:#4F46E5;">Course Structure:</h4>
                            <ul style="list-style-type: none; padding-left: 0; margin: 0;">
                                <li>📌 Week 1: Advanced SQL</li>
                                <li>📌 Week 2: Database Deployment</li>
                                <li>📌 Week 3: ML Algorithms</li>
                                <li>📌 Week 4: Real-time Systems</li>
                                <li>📌 Week 5: Cloud Integration</li>
                                <li>📌 Week 6: Capstone Project</li>
                            </ul>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Start Course 2 →", key="course2"):
                    st.session_state["page"] = "loginx"
                    st.rerun()
            
            with col2:
                st.markdown("""
                    <div class="svg-container">
                        <img src="https://www.svgrepo.com/show/373829/ai.svg" 
                             style="width:100%; height:100%; object-fit:cover;">
                    </div>
                """, unsafe_allow_html=True)

show()
