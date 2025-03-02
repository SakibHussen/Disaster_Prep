from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

import requests

app = Flask(__name__)

# Set your Google Gemini API key
GEMINI_API_KEY = "AIzaSyCQXa7a4EtOu53QiZNu0mIszdtjsTGIfSk"
genai.configure(api_key=GEMINI_API_KEY)

genai.configure(api_key=GEMINI_API_KEY)



YOUR_API_KEY="AIzaSyAkcVveoJt2Csz0PCubyVdIeNfe1s76058"




def get_disaster_risk(lat, lon):
    try:
        
        url = f"https://api.example.com/getDisasterRisk?lat={lat}&lon={lon}&key={YOUR_API_KEY}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"⚠️ Error: Received status code {response.status_code}. Using default values.")
            return {"flood": 3, "earthquake": 3, "tsunami": 3, "wildfire": 3, "hurricane": 3}

        risk_data = response.json()
        return {
            "flood": risk_data.get("flood_risk", 3),
            "earthquake": risk_data.get("earthquake_risk", 3),
            "tsunami": risk_data.get("tsunami_risk", 3),
            "wildfire": risk_data.get("wildfire_risk", 3),
            "hurricane": risk_data.get("hurricane_risk", 3)
        }

    except requests.exceptions.RequestException as e:
        print(f"⚠️ API Request Failed: {e}. Using default values.")
        return {"flood": 3, "earthquake": 3, "tsunami": 3, "wildfire": 3, "hurricane": 3}



def translate_text(text, target_language):
    url = f"https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "target": target_language,
        "format": "text",
        "key": YOUR_API_KEY
    }
    response = requests.post(url, data=params)
    response.raise_for_status() 
    
    if response.status_code == 200:
        translated_text= response.json()["data"]["translations"][0]["translatedText"]
        return translated_text
    else:
        print(f"⚠️ Translation Failed: Received status code {response.status_code} - {response.text}")
        return text 


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_preparedness', methods=['POST'])
def predict_preparedness():
    data = request.json
    user_data = data.get("selected_items", [])
    location = data.get("location", {})
    selected_language = data.get("language", "en")

    lat, lon = location.get("latitude"), location.get("longitude")

    if lat and lon:
        DISASTER_RISK_LEVELS = get_disaster_risk(lat, lon)
    else:
        DISASTER_RISK_LEVELS = {"flood": 3, "earthquake": 3, "tsunami": 3, "wildfire": 3, "hurricane": 3}

   
    ITEM_WEIGHTS = {
        "flashlight": {"flood": 4, "earthquake": 4, "wildfire": 4, "hurricane": 4},
        "first-aid-kit": {"flood": 5, "earthquake": 5, "tsunami": 5, "wildfire": 5, "hurricane": 5},
        "water": {"flood": 5, "earthquake": 5, "tsunami": 5, "hurricane": 5},
        "radio": {"flood": 5, "earthquake": 5, "tsunami": 5, "wildfire": 5, "hurricane": 5}
    }

    
    disaster_scores = {disaster: 0 for disaster in DISASTER_RISK_LEVELS}
    max_possible_scores = {disaster: 0 for disaster in DISASTER_RISK_LEVELS}

    
    for item in user_data:
        if item in ITEM_WEIGHTS:
            for disaster, weight in ITEM_WEIGHTS[item].items():
                disaster_scores[disaster] += weight * DISASTER_RISK_LEVELS[disaster]

    
    for item_weights in ITEM_WEIGHTS.values():
        for disaster, weight in item_weights.items():
            max_possible_scores[disaster] += weight * DISASTER_RISK_LEVELS[disaster]

    
    preparedness_percentages = {
        disaster: round((disaster_scores[disaster] / max_possible_scores[disaster]) * 100, 2)
        for disaster in disaster_scores
    }

    
    prompt = f"""
    The user has selected these preparedness items: {user_data}.
    Their preparedness scores: {preparedness_percentages}.
    Their location-based risk levels: {DISASTER_RISK_LEVELS}.
    Provide an analysis of their readiness and suggest improvements.

    ### Format Guidelines:
    - Use `<h2>`, `<h3>`, `<ul>`, `<li>`, and `<p>` for proper HTML formatting.
    - Ensure the response is **clear and structured**.
    - **Do NOT include raw backticks (`) or code blocks.**
    """

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    ai_feedback = response.text
    if selected_language != "en":
        ai_feedback = translate_text(ai_feedback, selected_language)
        
    return render_template('result.html', ai_feedback=ai_feedback, latitude=lat, longitude=lon, language=selected_language)



if __name__ == '__main__':
    app.run(debug=True)