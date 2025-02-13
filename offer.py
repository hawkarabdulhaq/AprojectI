import streamlit as st
import base64

def add_shine_effect(text, color):
    return f"""
    <div style="
        background: linear-gradient(90deg, {color}22 0%, {color} 50%, {color}22 100%);
        background-size: 200% 100%;
        animation: shine 2s infinite;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    ">
        <h1 style="color: {color}; margin: 0; font-size: 3.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">
            {text}
        </h1>
    </div>
    <style>
        @keyframes shine {
            0% {background-position: -100% 0;}
            100% {background-position: 100% 0;}
        }
    </style>
    """

def show_offer():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .week-highlight {
            color: #2E86C1;
            font-weight: bold;
        }
        .impact-section {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .availability {
            background-color: #e8f4f9;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with shine effect
    st.markdown(add_shine_effect("AI for Impact", "#FF9966"), unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #666;'>What We Offer</h2>", unsafe_allow_html=True)

    # Create tabs with custom styling
    course_tabs = st.tabs([
        "🔰 Course 1: Foundations of Python Programming",
        "🚀 Course 2: Advanced Machine Learning"
    ])

    # Course 1 Tab
    with course_tabs[0]:
        st.markdown("<h2 style='color: #2E86C1;'>Foundations of Python Programming and Applied Coding</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="impact-section">
        <h3>🎯 Impact</h3>
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
        📌 <b>Availability:</b> ✅ Included in Basic, Pro, and VIP Plans
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Learning", key="start_course1", use_container_width=True):
            import login
            login.show_login_create_account()

    # Course 2 Tab
    with course_tabs[1]:
        st.markdown("<h2 style='color: #2E86C1;'>Advanced Machine Learning and Real-Time Deployment</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="impact-section">
        <h3>🎯 Impact</h3>
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
        📌 <b>Availability:</b> ✅ Included in Pro and VIP Plans (Not available in Basic Plan)
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Learning", key="start_course2", use_container_width=True):
            import loginx
            loginx.show_login_create_account()

if __name__ == "__main__":
    show_offer()
