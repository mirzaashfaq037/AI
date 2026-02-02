import streamlit as st
import pandas as pd

# Set page config for a professional look
st.set_page_config(page_title="AI Learning Engine", page_icon="🎓")

# 1. DATABASE: Educational resources tagged by topic
@st.cache_data # Caches data for better performance
def load_data():
    content_data = {
        'Topic': ['Variables', 'Variables', 'Loops', 'Loops', 'Functions', 'Functions'],
        'Title': ['Intro to Python Variables', 'Advanced Data Types', 'Understanding For-Loops', 'While-Loops Mastery', 'Defining Functions', 'Return Statements in Python'],
        'Link': ['https://link1.com', 'https://link2.com', 'https://link3.com', 'https://link4.com', 'https://link5.com', 'https://link6.com']
    }
    return pd.DataFrame(content_data)

df_content = load_data()

# 2. UI HEADER
st.title("🎓 AI Personalized Learning Engine")
st.write("This engine adapts to your performance. Take the quiz to identify your knowledge gaps.")

# 3. QUIZ SECTION
with st.form("quiz_form"):
    st.subheader("Knowledge Assessment")
    
    # We use None as default to ensure the user actually picks an answer
    q1 = st.radio("1. Which keyword is used to start a loop?", ["None", "var", "for", "def"], index=0)
    q2 = st.radio("2. How do you store a value in Python?", ["None", "x = 5", "store 5 in x", "x : 5"], index=0)
    q3 = st.radio("3. Which keyword defines a function?", ["None", "func", "lambda", "def"], index=0)
    
    submitted = st.form_submit_button("Analyze Performance & Generate Path")

# 4. PERSONALIZATION LOGIC
if submitted:
    if "None" in [q1, q2, q3]:
        st.warning("Please answer all questions before submitting.")
    else:
        gaps = []
        score = 0
        
        # Grading Logic
        if q1 == "for": score += 1
        else: gaps.append("Loops")
            
        if q2 == "x = 5": score += 1
        else: gaps.append("Variables")
            
        if q3 == "def": score += 1
        else: gaps.append("Functions")
        
        st.divider()
        
        # Display Results
        st.subheader(f"Your Score: {score}/3")
        
        if score == 3:
            st.success("🎉 Perfect score! You have mastered these introductory topics.")
            st.balloons()
        else:
            st.error(f"We identified gaps in your understanding of: **{', '.join(gaps)}**")
            
            st.subheader("📚 Your Personalized Learning Path")
            st.write("The AI has curated these specific resources to help you improve:")
            
            # Filter database for recommended content based on 'gaps'
            recommendations = df_content[df_content['Topic'].isin(gaps)]
            
            for index, row in recommendations.iterrows():
                with st.expander(f"Recommended for {row['Topic']}: {row['Title']}"):
                    st.write(f"This resource specifically targets your weakness in **{row['Topic']}**.")
                    st.link_button("Go to Resource", row['Link'])