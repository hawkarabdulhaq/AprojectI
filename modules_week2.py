import streamlit as st
import pandas as pd

def show():
    # Create 12 tabs with proper comma separation between each tab name.
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs([
    "the Scale up Week",
    "2.1 Breaking Down Scripts!",
    "2.2 Quiz",
    "2.3 Scale up scripts",
    "2.4 Merging & Reversing",
    "2.5 G.C for Researchers",
    "2.6 Case Study",
    "2.7 Limitations of G.C",
    "2.8 Google Sheets API",
    "2.9 GitHub for webapp",
    "Assignment 3",
    "Assignment 4"
])


    with tab1:
        st.header("Welcome to the Scale up Week")
        st.video("https://youtu.be/OC1J2uZlLdQ")
        
    with tab2:
        st.header("2.1 Breaking Down Long Scripts and Using Google Drive with Google Colab")
    
        st.subheader("Purpose:")
        st.write(
        "Splitting long scripts into smaller, modular scripts improves code readability, reusability, and debugging efficiency. "
        "Google Drive acts as cloud storage for these scripts, making them accessible across devices and enabling integration with Google Colab for seamless execution."
    )
    
        st.video("https://youtu.be/d79b7IFY6dM")
    
        st.image("https://github.com/Hakari-Bibani/AprojectI/blob/main/workflow.png")
    
        st.subheader("Steps:")
        st.markdown(
        """
**<span style="color: #ADD8E6;">Break Down the Script:</span>**
- Identify distinct functionalities within the script (e.g., data processing, plotting, utilities).
- Save each functionality as a separate Python file (.py) with a clear, descriptive name.

**<span style="color: #ADD8E6;">Store in Google Drive:</span>**
- Create a folder in Google Drive to store these smaller scripts.
- Organize the scripts into folders if needed (e.g., utilities, visualizations).

**<span style="color: #ADD8E6;">Mount Google Drive in Colab:</span>**
- Mount Google Drive to access files directly from Colab.
- Append the script directory to the Python system path so the scripts can be imported as modules.

**<span style="color: #ADD8E6;">Use Scripts in Colab:</span>**
- Import the required scripts in Colab using Python's import statement.
- Reload any updated scripts dynamically without restarting the notebook.

**<span style="color: red;">Benefits:</span>**
- **Modularity:** Easier to manage, test, and debug smaller scripts.
- **Reusability:** Individual scripts can be reused across multiple projects.
- **Cloud Access:** Store scripts in Google Drive for persistent and cross-device availability.
- **Collaboration:** Allows multiple contributors to work on different parts of the code simultaneously.
- **Efficiency:** Faster updates and testing of specific functionalities without running the entire script.
        """,
        unsafe_allow_html=True
    )


    with tab3:
        import quiz2
        quiz2.show()

    with tab4:
        st.header("2.3 Scale up your scripts Recorded Session")
        st.video("https://youtu.be/55VfpKxvp7s")
        st.markdown("### Presentation:")
        st.components.v1.html(
        """
        <iframe src="https://docs.google.com/presentation/d/1iOFdiLq3Wgpvnz1cjh_sEMSUZ68fngOCa5ShWFLA1OA/embed?start=false&loop=false&delayms=3000" 
        frameborder="0" width="800" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """,
        height=600,
    )



    with tab6:
        st.header("2.5 Google Colab for Researchers: A Beginner-Friendly Tool for Advanced Insights")
    
        st.write(
        "Google Colab is a powerful tool for researchers across various fields, offering a free and user-friendly platform for coding, data analysis, and collaboration. Even if you're not familiar with coding, Colab makes advanced computational tasks more accessible. Here's why researchers love Google Colab and how it enhances research credibility:"
    )
    
         st.markdown(
        """
**<span style="color: #ADD8E6;">Why Use Google Colab in Research?</span>**

- **<span style="color: #FFA07A;">No Installation Needed:</span>**  
  Google Colab runs entirely in your browser. You don't need to install Python or any additional software, making it incredibly easy to get started.

- **<span style="color: #FFA07A;">Free Access to Powerful Resources:</span>**  
  Google Colab provides access to cloud-based computing resources, including free GPUs (graphics processing units). This allows researchers to process large datasets and run complex algorithms without needing expensive hardware.

- **<span style="color: #FFA07A;">Collaborative Features:</span>**  
  Similar to Google Docs, multiple researchers can work together in real-time on the same notebook. This fosters teamwork and transparency in research.

- **<span style="color: #FFA07A;">Credibility in Research:</span>**  
  By using Google Colab, you can save and share your code, datasets, and results. This transparency ensures reproducibility—a cornerstone of credible scientific research.

- **<span style="color: #FFA07A;">Wide Support for Libraries and Tools:</span>**  
  Colab supports popular Python libraries like NumPy, Pandas, and Matplotlib, which are essential for data analysis. It also integrates easily with machine learning and geospatial tools like TensorFlow, Scikit-learn, and Google Earth Engine.

**<span style="color: #ADD8E6;">Benefits for Different Research Areas:</span>**

- **<span style="color: #FFA07A;">Geoscience Researchers:</span>**  
  Use Colab to analyze geological data, visualize seismic waves, or process geospatial information with Google Earth Engine.  
  *Example: Visualizing land use changes over time with satellite data.*

- **<span style="color: #FFA07A;">Medical Researchers:</span>**  
  Process patient datasets, develop machine learning models for disease prediction, or analyze genetic data with bioinformatics tools.  
  *Example: Training a machine learning model to detect anomalies in medical imaging.*

- **<span style="color: #FFA07A;">Social Science Researchers:</span>**  
  Analyze survey data, explore public opinion trends, or map demographic information using Colab's visualization tools.  
  *Example: Creating interactive maps of population density and urban development.*

- **<span style="color: #FFA07A;">Environmental Researchers:</span>**  
  Model climate change patterns, analyze water quality data, or study biodiversity distribution using Colab's Python-based libraries.  
  *Example: Running a simulation to predict future climate scenarios based on historical data.*

- **<span style="color: #FFA07A;">Business and Economic Researchers:</span>**  
  Conduct statistical analysis, forecast market trends, or visualize financial data.  
  *Example: Building a predictive model for stock market movements.*

**<span style="color: #ADD8E6;">How Researchers Benefit from Google Colab:</span>**

- **Improved Efficiency:** Automate repetitive tasks like data cleaning and visualization.
- **Enhanced Credibility:** Share your research notebooks to allow others to replicate your work.
- **Cost Savings:** Use free resources instead of investing in expensive software or hardware.
- **Community Support:** Access a wealth of tutorials and community-driven solutions to solve your challenges.

**Conclusion:**  
Google Colab bridges the gap between researchers and advanced technology, empowering you to tackle complex problems without needing extensive coding expertise. It’s a versatile tool that can significantly enhance the quality and impact of your research, no matter your field of study. Start exploring Google Colab today and elevate your research potential!
        """,
        unsafe_allow_html=True
    )


    with tab7:
        import as3
        as1.show()

    with tab8:
        st.header("1.8 Understanding APIs: The Key to Real-Time Data Integration")
        st.markdown("<h3 style='color: goldenrod;'>What is an API?</h3>", unsafe_allow_html=True)
        st.write(
            "An API (Application Programming Interface) is a set of rules and protocols that allows different software applications "
            "to communicate with each other. Think of it as a bridge that lets one piece of software request and retrieve data or services "
            "from another. APIs define how requests for information or actions are made, the format of these requests, and the expected responses, "
            "allowing applications to interact without needing to understand the inner workings of each other."
        )
        st.markdown("<h3 style='color: goldenrod;'>Why is an API Important?</h3>", unsafe_allow_html=True)
        st.write(
            "APIs are crucial because they enable software systems to share data and functionality, which is especially useful for developers "
            "and organizations. With APIs, applications can be made more powerful and flexible by integrating external data or services. "
            "This ability to pull in real-time data from other platforms, or let users perform specific tasks from different systems without leaving "
            "the primary application, enhances user experiences and broadens application capabilities."
        )
        st.markdown("<h3 style='color: goldenrod;'>How is an API Used? (Example)</h3>", unsafe_allow_html=True)
        st.write(
            "To use an API, you usually send a request to an endpoint URL with specific parameters that define what data or action you’re interested in. "
            "Let’s use the USGS Earthquake API as an example:"
        )
        st.code(
            "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=YYYY-MM-DD&endtime=YYYY-MM-DD",
            language="bash"
        )
        st.write("Here’s a breakdown of each part:")
        st.write("• **https://earthquake.usgs.gov/fdsnws/event/1/query:** This is the endpoint URL where the API is hosted.")
        st.write("• **format=geojson:** This parameter specifies that the response should be in GeoJSON format, a format for encoding geographical data.")
        st.write("• **starttime=YYYY-MM-DD and endtime=YYYY-MM-DD:** These parameters allow you to set a date range for the data, where YYYY-MM-DD should be replaced with actual dates (e.g., starttime=2024-01-01&endtime=2024-01-31 to get data for January 2024).")
        st.write(
            "When a request is sent with the filled-in parameters, the API returns data, often in JSON format, containing details about all recorded "
            "earthquakes within that time range. Each record includes information such as location, magnitude, depth, and time."
        )
        st.markdown("<h3 style='color: goldenrod;'>Why Use an API Like the USGS Earthquake API?</h3>", unsafe_allow_html=True)
        st.write(
            "Using APIs like the USGS Earthquake API allows developers to pull in constantly updated earthquake data directly into their applications "
            "without manually collecting, processing, and updating it themselves. This real-time data can be visualized on maps, used in alerts, "
            "or integrated into research dashboards."
        )

    with tab9:
        import as4
        as2.show()

    with tab10:
        st.markdown("<h1 style='color:gold;'>1.10 Real-Time Applications of Google Colab</h1>", unsafe_allow_html=True)
        st.write(
            "Google Colab is a powerful cloud-based platform that enables researchers, students, and professionals to execute Python code directly in their browsers. "
            "Its versatility makes it a valuable tool for solving real-world problems in various fields. Below are some fascinating real-time applications of Google Colab:"
        )
        st.markdown(
            "• **Real-Time Voice Cloning:** Using pre-trained models, users can clone voices from audio samples and generate new speech. "
            "This is helpful in personalized speech synthesis and assistive technologies. "
            "[Explore an example here](https://colab.research.google.com/github/tugstugi/dl-colab-notebooks/blob/master/notebooks/RealTimeVoiceCloning.ipynb)"
        )
        st.markdown(
            "• **Real-Time Object Detection:** Implement models like YOLO (You Only Look Once) for real-time object detection. "
            "Applications include autonomous vehicles and surveillance systems. "
            "[Learn more here](https://expertbeacon.com/real-time-object-detection-using-yolo-in-google-colab/)"
        )
        st.markdown(
            "• **Real-Time Data Analysis and Visualization:** Colab allows users to connect to live data sources for immediate processing and visualization, "
            "enabling faster decision-making in fields like finance and research."
        )
        st.markdown(
            "• **Collaborative Coding and Education:** Google Colab's real-time collaboration feature is ideal for educators and teams working together on coding projects. "
            "This makes it a powerful tool for interactive learning and group tasks. "
            "[Explore more here](https://devpost.com/software/actually-colab-real-time-collaborative-jupyter-editor)"
        )
        st.markdown(
            "• **Real-Time Machine Learning Model Training:** Leverage GPUs and TPUs for faster training of machine learning models. "
            "Colab supports iterative development, making it a go-to platform for AI and data science projects."
        )
        st.write(
            "These applications demonstrate how Google Colab can enhance your research, learning, and development processes. "
            "Its real-time capabilities and collaborative features make it a valuable asset for tackling complex challenges and exploring innovative solutions."
        )

    with tab11:
        import quiz2
        quiz1.show()
        
    with tab12:
        import quiz3
        quiz1.show()

if __name__ == "__main__":
    show()
