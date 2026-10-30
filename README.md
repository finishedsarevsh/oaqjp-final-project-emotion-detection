# Emotion Detector

An AI-based web application that uses IBM Watson NLP to detect emotions from text input. Built as the final project for the IBM AI-Based Web App Development course.

## Features

- Detects five emotions: anger, disgust, fear, joy, and sadness
- Identifies the dominant emotion in any given text
- REST API via Flask with a browser-based UI
- Unit-tested with Python `unittest`
- Clean code with Pylint 10/10 score

## Tech Stack

- Python 3.11
- IBM Watson NLP (EmotionPredict endpoint)
- Flask (web framework)
- Requests (HTTP client)
- Pylint (static analysis)

## Setup

```bash
pip install flask requests
python server.py
```

Then open http://localhost:5000 in your browser.

## Project Structure

```
oaqjp-final-project-emotion-detection/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
```
