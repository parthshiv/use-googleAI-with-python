# Jarvis — AI Voice Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight desktop **Jarvis** voice assistant that listens for a wake word, runs commands (open websites, show maps/directions), and uses **Google Gemini** for conversational replies. This README assumes your main script is `main.py`.

---

## Features

- 🎤 Wake-word activation (e.g., **"Jarvis"**, **"Hey Jarvis"**)  
- 🌐 Open websites (Google, YouTube, Instagram, Facebook, etc.)  
- 🗺️ Open a place in Google Maps (e.g., *"Jarvis show me Taj Mahal in map"*)  
- 🚗 Open directions in Google Maps (e.g., *"Jarvis show me direction from Ahmedabad to Mumbai in map"*)  
- 🔊 Text-to-speech via **gTTS** and playback with **pygame**  
- 🤖 Fallback / conversational replies using **Google Gemini**  
- ⚙️ Adjustable microphone & recognition tuning for low-latency responses

---

## Project layout

    project/
    ├─ main.py
    ├─ googleAI-key.txt # your Google AI Studio API key (DO NOT commit)
    ├─ command.mp3 # generated TTS file (ignored)
    ├─ README.md
    ├─ requirements.txt
    └─ .gitignore

---

## Requirements

Tested with Python 3.10+. Install required Python packages:

```bash
pip install SpeechRecognition gTTS pygame google-genai
```
Microphone support (Windows)

If pyaudio is required and fails to install:
```bash
pip install pipwin
pipwin install pyaudio
```
Setup

Create googleAI-key.txt in the project root and paste your Google AI Studio API key (one line).

Add googleAI-key.txt and command.mp3 to .gitignore.

Install dependencies (see Requirements).

Run Jarvis:
```bash

python main.py
```


Jarvis should announce initialization and begin listening. Use the wake word, then give a command.

## Example voice commands

# Websites

Jarvis open Google

Jarvis open YouTube

# Maps & Directions

Jarvis show me Taj Mahal in map

Jarvis show me Ahmedabad in map

Jarvis show me direction from Surat to Pune in map

# AI Q&A

Jarvis, what is artificial intelligence?

Jarvis, tell me a joke.

# Tuning (for snappy responses)

Edit main.py recognizer settings:

```bash
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.6
recognizer.non_speaking_duration = 0.2

# Use listen(timeout=1, phrase_time_limit=2) to keep latency low

Increase energy_threshold in noisy environments.

Decrease it if the assistant misses quiet speech.

Handling time-sensitive queries

Models have static knowledge and may be out-of-date. For questions like “Who is the president” or stock prices, implement a web verification step (e.g., scrape Wikipedia or use a news API) and return the verified fact (optionally pass it to Gemini for formatting).
```

# Contribution

PRs welcome. Ideas:

Add offline STT (Vosk + webrtcvad) for lower latency

Add hotword detection (Porcupine)

Integrate weather, calendar, or home automation

## License

MIT License — see LICENSE file.
