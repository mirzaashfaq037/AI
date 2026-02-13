**🚀 Key Features**

•	🤖 AI-Powered Knowledge Assessment: Uses quiz scoring logic to identify weak topics in programming fundamentals.
•	📊 Interactive Dashboard: Learners interact through a user-friendly Streamlit interface.
•	📄 Automated Learning Path: Curates content based on detected knowledge gaps.
•	🛡️ Real-time Feedback: Provides instant scores, topic gaps, and resource links.
________________________________________
📂 Dataset / Content
The system uses a small in-memory database of educational resources tagged by topic:
•	Topics: Variables, Loops, Functions
•	Content Examples:
o	Intro to Python Variables
o	Advanced Data Types
o	Understanding For-Loops
o	While-Loops Mastery
o	Defining Functions
o	Return Statements in Python
Optional: Can be extended with CSV files or larger datasets of tutorials, videos, and interactive exercises.
________________________________________
🛠️ Installation & Setup
Follow these steps to run the project locally:
1.	Clone the Repository
git clone https://github.com/YOUR-USERNAME/ai-learning-engine.git
cd ai-learning-engine
2.	Install Dependencies
pip install pandas streamlit numpy
3.	Run the Application
streamlit run app.py
# Or if you face issues:
python -m streamlit run app.py
________________________________________
🧠 How It Works
1.	Quiz Assessment: Learners answer multiple-choice questions on programming fundamentals.
2.	Knowledge Gap Detection: The engine evaluates responses and identifies weak topics.
3.	Resource Recommendation: Filters educational resources that target the learner’s gaps.
4.	Feedback Display: Learners see scores, knowledge gaps, and clickable links to resources.
________________________________________
📂 Project Structure
ai_learning_engine/
│
├── app.py           # Streamlit dashboard for quiz and recommendations

├── resources.csv    # Optional: Database of educational content

├── requirements.txt # Python dependencies
Core Components:

•	app.py: Main Streamlit application with quiz, scoring, and recommendations.

•	resources.csv (optional): Expandable database for educational content.
________________________________________

