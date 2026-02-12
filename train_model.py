# train_model.py
import pandas as pd
import joblib

# -------------------------------
# 1. Define Quiz Questions & Correct Answers
# -------------------------------
quiz_data = {
    'question': [
        "Which keyword is used to start a loop?",
        "How do you store a value in Python?",
        "Which keyword defines a function?"
    ],
    'options': [
        ["var", "for", "def", "None"],
        ["x = 5", "store 5 in x", "x : 5", "None"],
        ["func", "lambda", "def", "None"]
    ],
    'correct_answer': [
        "for",
        "x = 5",
        "def"
    ],
    'topic': [
        "Loops",
        "Variables",
        "Functions"
    ]
}

# Convert to DataFrame for easier handling
df_quiz = pd.DataFrame(quiz_data)

# -------------------------------
# 2. Define Simple Scoring Model
# -------------------------------
# We'll map correct answers to a score for each topic
# This is a lightweight "model" to simulate AI scoring
def evaluate_quiz(user_answers):
    """
    user_answers: dict with question index -> answer
    returns: score, list of gaps
    """
    score = 0
    gaps = []

    for idx, correct in enumerate(df_quiz['correct_answer']):
        if user_answers.get(idx) == correct:
            score += 1
        else:
            gaps.append(df_quiz.loc[idx, 'topic'])

    return score, gaps

# Save the model to a file using joblib
joblib.dump({
    'quiz_df': df_quiz,
    'evaluate_quiz': evaluate_quiz
}, 'learning_model.pkl')

print("🎉 Success! 'learning_model.pkl' file created.")
