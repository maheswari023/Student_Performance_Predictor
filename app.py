import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page configuration
st.set_page_config(page_title="Student Performance Predictor", layout="wide")

# Custom styles
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
        body, .stApp {
            background-color: #1e3c72 !important;
            background-image: linear-gradient(to right, #1e3c72, #2a5298) !important;
            color: white !important;
            font-family: 'Segoe UI', sans-serif;
        }

        .header-container {
            width: 100%;
            padding: 30px 20px 10px 20px;
            background-color: #0f172a;
            text-align: center;
            border-bottom: 1px solid #334155;
        }

        .header-title {
            font-size: 2.5rem;
            color: #facc15;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .nav-links a {
            margin: 0 18px;
            color: #93c5fd;
            text-decoration: none;
            font-size: 1.1rem;
            font-weight: bold;
        }

        .nav-links a:hover {
            color: #ffffff;
            text-decoration: underline;
        }

        .card {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            margin: 60px auto;
            text-align: center;
        }

        label {
            font-weight: bold !important;
            color: white !important;
        }

        input, select {
            width: 100%;
            padding: 12px;
            margin: 12px 0 25px 0;
            border-radius: 10px;
            border: 1px solid #475569;
            font-size: 15px;
            color: white !important;
            background-color: #1f2937 !important;
        }

        .predict-button {
            background-color: #3b82f6;
            color: white;
            font-weight: bold;
            padding: 14px;
            border-radius: 10px;
            width: 100%;
            font-size: 16px;
            border: none;
        }

        .predict-button:hover {
            background-color: #2563eb;
        }

        .result {
            background-color: #059669;
            padding: 16px;
            margin-top: 25px;
            border-radius: 12px;
            font-size: 18px;
            color: white;
        }

        footer {
            margin-top: 60px;
            padding: 20px;
            background-color: #0f172a;
            color: #cbd5e1;
            text-align: center;
            font-size: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# 🎓 Header and Navigation
st.markdown('''
<div class="header-container">
    <div class="header-title">🎓 Student Performance Predictor</div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#predict">Predict</a>
    </div>
</div>
''', unsafe_allow_html=True)

# Home Section
st.markdown('''
<div id="home">
    <div class="card">
        <h3>👋 Welcome!</h3>
        <p>This web app predicts a student’s average final exam score based on their reading and writing scores using machine learning.</p>
    </div>
</div>
''', unsafe_allow_html=True)

#  About Section 
st.markdown('''
<div class="card" id="about">
    <h4>📌 About</h4>
    <p>This ML project uses a regression model to predict student exam scores based on academic metrics.</p>
    <p>Built using Python, Streamlit, and Scikit-learn — simple yet powerful.</p>
</div>
''', unsafe_allow_html=True)

# Prediction Section
st.markdown('<div class="card" id="predict">', unsafe_allow_html=True)
st.markdown("<h4>📊 Enter student details to predict final average exam score</h4>", unsafe_allow_html=True)

with st.form("predict_form"):
    reading_score = st.text_input("📘 Reading Score (0-100)", placeholder="e.g. 85")
    writing_score = st.text_input("✍️ Writing Score (0-100)", placeholder="e.g. 78")
    test_prep = st.selectbox("🧪 Test Preparation Completed?", ["completed", "none"])
    predict_btn = st.form_submit_button("🔮 Predict Final Score")

    if predict_btn:
        try:
            r = float(reading_score)
            w = float(writing_score)
            p = 1 if test_prep == "completed" else 0
            df = pd.DataFrame([[r, w, p]], columns=["reading score", "writing score", "test_prep_done"])
            result = model.predict(df)[0]
            st.markdown(f'<div class="result">🎯 Predicted Final Exam Score: <strong>{round(result, 2)} / 100</strong></div>', unsafe_allow_html=True)
        except:
            st.error("❌ Please enter valid numeric values for reading and writing scores.")
st.markdown('</div>', unsafe_allow_html=True)

# 🔚 Footer
st.markdown('<footer>Built with ❤️ using Streamlit | 2025</footer>', unsafe_allow_html=True)
