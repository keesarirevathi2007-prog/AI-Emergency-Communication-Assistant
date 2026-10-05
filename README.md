# AI-Based Offline Emergency Communication Assistant

## 📌 Project Overview

The AI-Based Offline Emergency Communication Assistant is a web-based application designed to provide basic emergency guidance without requiring an internet connection.

The system allows users to describe an emergency situation and receive locally stored guidance based on the type of emergency detected.

## 🎯 Objectives

- Provide basic emergency guidance without internet access.
- Identify common emergency situations from user messages.
- Provide quick responses using locally stored information.
- Support voice input for describing emergencies.
- Provide important emergency contact numbers in India.

## 🚨 Emergency Situations Supported

The assistant can identify situations such as:

- 🏥 Medical emergencies
- 🔥 Fire emergencies
- 🚗 Road accidents
- ⚠️ Safety and danger situations
- 👤 Missing-person situations
- 🌪️ Natural disasters
- 🆘 General emergency requests

## ✨ Features

### 📴 Offline Support
The emergency guidance is stored locally, allowing the application to provide responses without depending on an internet connection.

### 🤖 Emergency Detection
The application analyzes the user's message and identifies the type of emergency using locally implemented keyword-based detection.

### 🎤 Voice Input
Users can describe an emergency using voice input through the browser.

### 📞 Emergency Contacts
The application provides important emergency numbers in India:

- 112 - Emergency Services
- 100 - Police
- 101 - Fire
- 108 - Ambulance

### ⚡ Fast Response
The application provides locally stored emergency guidance quickly after receiving the user's message.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## 📁 Project Structure

```text
AI-Emergency-Communication-Assistant/
│
├── app.py
├── emergency_assistant.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js