# Disaster_check
This is the project for Henhacks 2025!
# Disaster Preparedness AI Application

## Overview
This project is an AI-powered Disaster Preparedness Assessment Tool designed to help users evaluate their readiness for natural disasters based on selected survival items and their geographic location. The application utilizes AI analysis, Google Maps API for geolocation, and Google Translate API for multilingual support.

## Features
- 📍 **Location-Based Risk Assessment**: Users' risk levels are determined based on their latitude and longitude.
- 🎯 **Personalized Preparedness Score**: Calculates preparedness scores based on selected survival items and disaster risk levels.
- 📝 **AI-Powered Recommendations**: Uses Google's Gemini AI to analyze user preparedness and provide improvement suggestions.
- 🌍 **Multilingual Support**: Google Translate API enables translation of AI analysis into multiple languages.
- 🗺️ **Google Maps Integration**: Displays user location on an interactive map.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **APIs**:
  - Google Maps API
  - Google Translate API
  - Gemini AI API
- **Hosting**: Local development for submission

## Installation & Setup
### 1️⃣ Prerequisites
Ensure you have Python installed and the following dependencies:

```bash
pip install -r requirements.txt
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/DisasterPreparednessAI.git
cd DisasterPreparednessAI
```

### 3️⃣ Setup Environment Variables
Create a `.env` file and add your API keys:

```ini
GOOGLE_API_KEY=your_google_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 4️⃣ Run the Flask App
```bash
python app.py
```

The app will run locally on `http://127.0.0.1:5000`

## API Endpoints
### `GET /`
- Serves the survey form for disaster preparedness.

### `POST /predict_preparedness`
- Accepts user-selected survival items and location data.
- Calls AI model to analyze preparedness.
- Translates the response if necessary.

## Usage Guide
1️⃣ Open `http://127.0.0.1:5000` in your browser.
2️⃣ Select preparedness items.
3️⃣ Allow location access.
4️⃣ Choose your preferred language.
5️⃣ Click "Submit" to receive AI-generated recommendations and see your location on the map.

## Contribution
- Fork the repo & clone it.
- Create a new branch: `git checkout -b feature-branch`
- Commit your changes: `git commit -m 'Add new feature'`
- Push the changes: `git push origin feature-branch`
- Open a Pull Request!

## License
This project is licensed under the MIT License.

## Acknowledgments
- Google APIs (Maps, Translate)
- OpenAI Gemini Model
- Flask Community

