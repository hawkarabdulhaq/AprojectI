import streamlit as st

def create_programming_svg() -> str:
    """Return SVG markup for the programming course icon."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="180" height="180" class="course-icon">
        <defs>
            <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#3A416F;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#141727;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="lineGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#4FD1C5;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#2DD4BF;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="120" cy="120" r="110" fill="url(#bgGrad1)" />
        <path d="M80,80 L110,110 L80,140" stroke="url(#lineGrad1)" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M160,80 L130,110 L160,140" stroke="url(#lineGrad1)" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="120" cy="110" r="8" fill="#4FD1C5"/>
        <g class="floating-circles" opacity="0.6">
            <circle cx="90" cy="70" r="4" fill="#4FD1C5"/>
            <circle cx="150" cy="160" r="4" fill="#4FD1C5"/>
            <circle cx="170" cy="90" r="4" fill="#4FD1C5"/>
        </g>
    </svg>"""

def create_ml_svg() -> str:
    """Return SVG markup for the machine learning course icon."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="180" height="180" class="course-icon">
        <defs>
            <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#3A416F;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#141727;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="nodeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#F6AD55;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ED8936;stop-opacity:1" />
            </linearGradient>
        </defs>
        <circle cx="120" cy="120" r="110" fill="url(#bgGrad2)" />
        <g class="neural-network">
            <circle cx="120" cy="70" r="15" fill="url(#nodeGrad)"/>
            <circle cx="80" cy="120" r="15" fill="url(#nodeGrad)"/>
            <circle cx="160" cy="120" r="15" fill="url(#nodeGrad)"/>
            <circle cx="120" cy="170" r="15" fill="url(#nodeGrad)"/>
            <path d="M120,85 L80,105 M120,85 L160,105 M80,135 L120,155 M160,135 L120,155" 
                  stroke="#ED8936" stroke-width="3" opacity="0.6"/>
        </g>
    </svg>"""

def show() -> None:
    """Render the Streamlit application with course offers using HTML for better styling."""
    # Inject CSS styles
    st.markdown(
        """
<style>
/* Modern CSS Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Custom Animations */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}

@keyframes slideIn {
    from { transform: translateX(-50px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

/* Main Container Styles */
.main-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    background: linear-gradient(180deg, #F8FAFC 0%, #EDF2F7 100%);
    min-height: 100vh;
}

/* Header Styles */
.hero-section {
    text-align: center;
    padding: 3rem 0;
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    border-radius: 20px;
    margin-bottom: 3rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.hero-title {
    font-size: 4rem;
    color: #F8FAFC;
    margin-bottom: 1rem;
    font-weight: 800;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    animation: slideIn 1s ease-out;
}

.hero-subtitle {
    font-size: 1.8rem;
    color: #94A3B8;
    font-weight: 500;
    animation: slideIn 1s ease-out 0.2s both;
}

/* Course Card Styles */
.course-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
    animation: slideIn 0.8s ease-out;
}

.course-card:hover {
    transform: translateY(-5px);
}

.course-icon {
    float: right;
    margin-top: -2rem;
    animation: float 6s ease-in-out infinite;
}

.course-title {
    font-size: 2.2rem;
    color: #1E293B;
    margin-bottom: 1.5rem;
    font-weight: 700;
}

.impact-section {
    background: #F1F5F9;
    padding: 1.5rem;
    border-radius: 15px;
    margin: 1.5rem 0;
}

.impact-title {
    color: #0F172A;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.impact-text {
    color: #475569;
    line-height: 1.6;
}

.chapters-section {
    margin: 2rem 0;
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
    background: linear-gradient(135deg, #4FD1C5 0%, #2DD4BF 100%);
    color: white;
    border-radius: 50px;
    font-weight: 600;
    margin-top: 1.5rem;
    box-shadow: 0 4px 12px rgba(45, 212, 191, 0.2);
}

/* Button Styles */
.custom-button {
    display: inline-block;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #3A416F 0%, #141727 100%);
    color: white;
    border-radius: 50px;
    font-weight: 600;
    margin-top: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    box-shadow: 0 4px 12px rgba(20, 23, 39, 0.2);
}

.custom-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(20, 23, 39, 0.3);
}

/* Tab Styles */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    background: #F1F5F9;
    padding: 1rem;
    border-radius: 50px;
    margin-bottom: 2rem;
}

.stTabs [data-baseweb="tab"] {
    padding: 1rem 2rem;
    border-radius: 50px;
    font-weight: 600;
    color: #475569;
    background: transparent;
    transition: all 0.3s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,255,255,0.5);
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: white;
    color: #1E293B;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
""",
        unsafe_allow_html=True,
    )

    # Render header section without extra indentation
    st.markdown(
        """
<div class="hero-section">
    <h1 class="hero-title">AI for Impact</h1>
    <h2 class="hero-subtitle">What We Offer</h2>
</div>
""",
        unsafe_allow_html=True,
    )

    # Create tabs for the courses
    tabs = st.tabs([
        "Course 1: Foundations of Python Programming",
        "Course 2: Advanced Machine Learning"
    ])

    with tabs[0]:
        st.markdown(
            f"""
<div class="course-card">
    {create_programming_svg()}
    <h2 class="course-title">Foundations of Python Programming and Applied Coding</h2>
    <div class="impact-section">
        <h3 class="impact-title">🎯 Impact</h3>
        <p class="impact-text">
            Participants gain foundational skills in Python programming and learn to create robust scripts,
            work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to
            automate tasks, process data, and build basic web applications.
        </p>
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
""", 
            unsafe_allow_html=True
        )
        if st.button("Start Course 1", key="btn1"):
            st.session_state["page"] = "login"
            st.experimental_rerun()

    with tabs[1]:
        st.markdown(
            f"""
<div class="course-card">
    {create_ml_svg()}
    <h2 class="course-title">Advanced Machine Learning and Real-Time Deployment</h2>
    <div class="impact-section">
        <h3 class="impact-title">🎯 Impact</h3>
        <p class="impact-text">
            Participants develop advanced skills in database management, machine learning, and real-time application deployment.
            This course focuses on practical implementations, enabling learners to create AI-driven solutions, deploy them in
            real-world scenarios, and integrate applications with cloud services.
        </p>
    </div>
    <div class="chapters-section">
        <h3 class="impact-title">📚 Course Chapters</h3>
        <div class="chapter-item">Week 1: Advanced SQL and Databases</div>
        <div class="chapter-item">Week 2: Deploy Database</div>
        <div class="chapter-item">Week 3: Unsupervised Machine Learning</div>
        <div class="chapter-item">Week 4: Supervised Machine Learning</div>
        <div class="chapter-item">Week 5: Real-Time Data Processing</div>
        <div class="chapter-item">Week 6: Capstone Project</div>
    </div>
    <div class="availability-badge">
        ✅ Included in Pro and VIP Plans (Not available in Basic Plan)
    </div>
</div>
""",
            unsafe_allow_html=True,
        )
        if st.button("Start Course 2", key="btn2"):
            st.session_state["page"] = "loginx"
            st.experimental_rerun()

if __name__ == "__main__":
    show()
