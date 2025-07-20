from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "burncheck_secret_key"

# Load the trained model
model = joblib.load("project3_burnout_model.pkl")

# Define input feature order (based on model training)
input_features = [
    'work_interfere', 'remote_work', 'tech_company', 'benefits', 'care_options',
    'wellness_program', 'seek_help', 'leave', 'anonymity', 'mental_health_consequence',
    'coworkers', 'supervisor',
    'family_history'
    
]

# ---- Routes ---- #

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/section2', methods=['GET', 'POST'])
def section2():
    previous_data = request.args.get('previous_data')
    if previous_data:
        previous_data = eval(previous_data)  # Converting back to dictionary
    else:
        previous_data = {}

    return render_template('section2.html', previous_data=previous_data)


@app.route('/section3', methods=['GET', 'POST'])
def section3():
    previous_data = request.args.get('previous_data')
    if previous_data:
        import ast
        previous_data = ast.literal_eval(previous_data)
    else:
        previous_data = {}

    return render_template('section3.html', previous_data=previous_data)


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        session['section3'] = request.form.to_dict()

        # Combine all form data
        all_data = {}
        for sec in ['section1', 'section2', 'section3']:
            all_data.update(session.get(sec, {}))

        # Convert inputs to numeric and in model's expected order
        input_array = []
        for feature in input_features:
            try:
                value = float(all_data.get(feature, 0))
            except ValueError:
                value = 0.0
            input_array.append(value)

        # Adjust input length
        expected_features = 23
        if len(input_array) < expected_features:
            input_array.extend([0.0] * (expected_features - len(input_array)))
        elif len(input_array) > expected_features:
            input_array = input_array[:expected_features]

        # Predict burnout score
        prediction_score = model.predict([input_array])[0]

        # Burnout levels
        level_map = {
            0: "Low",
            1: "Moderate",
            2: "High",
            3: "Critical"
        }
        prediction_level = level_map.get(prediction_score, "Unknown")

        # Identify top 3 contributing features
        feature_importance = model.feature_importances_ if hasattr(model, "feature_importances_") else [1]*len(input_features)
        top_indices = sorted(range(len(feature_importance)), key=lambda i: abs(input_array[i] * feature_importance[i]), reverse=True)[:3]
        top_factors = [input_features[i].replace("_", " ").capitalize() for i in top_indices]

        # Recommended tips (simple logic based on level)
        tips_dict = {
            "Low": ["Maintain your routine", "Take short breaks", "Stay connected with friends"],
            "Moderate": ["Incorporate meditation", "Talk to a mentor", "Avoid procrastination"],
            "High": ["Seek professional help", "Take time off", "Prioritize your tasks"],
            "Critical": ["Consult a counselor", "Immediate rest", "Speak to someone you trust"]
        }
        recommended_tips = tips_dict.get(prediction_level, [])

        # Motivation message
        motivation = {
            "Low": "You're on the right track. Keep taking care of yourself!",
            "Moderate": "Take it slow and steady – balance is key.",
            "High": "You're strong – with the right support, you’ll feel better soon.",
            "Critical": "Your health matters. Don’t hesitate to seek help immediately."
        }.get(prediction_level, "Take care of yourself.")

        # Pass all data to result.html
        return render_template('result.html',
                               prediction_score=prediction_score,
                               prediction_level=prediction_level,
                               top_factors=top_factors,
                               tips=recommended_tips,
                               message=motivation)

    else:
        # If someone visits /result directly via GET
        return redirect(url_for('index'))


        # 🔴 Log to CSV
        log_entry = all_data.copy()
        log_entry['prediction_level'] = result_label
        log_entry['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df_log = pd.DataFrame([log_entry])

        if not os.path.exists("burnout_form_log.csv"):
            df_log.to_csv("burnout_form_log.csv", index=False)
        else:
            df_log.to_csv("burnout_form_log.csv", mode='a', header=False, index=False)

        return render_template('result.html', result=result_label, prediction=prediction)

    return redirect(url_for('index'))

@app.route('/testmodel')
def test_model_predictions():
    test_cases = {
        "all_zeros": [0.0] * 23,
        "all_ones": [1.0] * 23,
        "all_threes": [3.0] * 23,
    }
    results = {name: int(model.predict([data])[0]) for name, data in test_cases.items()}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
