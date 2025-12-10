🚀 Jarvis – Voice Assistant (Google Gemini + Speech Recognition)

Jarvis is a lightweight desktop AI voice assistant that listens for a wake word, understands voice commands, opens apps/websites (Google, YouTube, Maps), gives directions, and answers general questions using Google Gemini.
Speech recognition is handled via SpeechRecognition + Google STT, while replies are spoken using gTTS + pygame.

✨ Features

🎤 Wake-word detection (e.g., "Jarvis", "Hey Jarvis")

🌐 Opens popular websites (Google, YouTube, Instagram, Facebook, etc.)

🗺️ Opens places or directions in Google Maps

Example: "Jarvis show me Taj Mahal in map"

Example: "Jarvis show me direction from Ahmedabad to Mumbai in map"

🤖 AI responses using Google Gemini 2.x models

🔊 Voice output using gTTS (Text-to-Speech)

🧠 Background listening with adjustable noise thresholds

📂 API key stored securely in a local file (googleAI-key.txt)

🧩 Extendable command system — easy to add new features

📦 Requirements

Install dependencies:

pip install SpeechRecognition gTTS pygame google-genai requests beautifulsoup4


You may also need PyAudio (for microphone access):

pip install pipwin
pipwin install pyaudio


If PyAudio installation fails, use pipwin — it installs the correct Windows wheel automatically.

🔐 API Key Setup

Create a file:

googleAI-key.txt


Paste your Google AI Studio API key inside it (one line only).
Do NOT commit this file to Git (add it to .gitignore).

▶️ Run the Assistant
python main.py


Jarvis will say:

“Initializing Jarvis…”

Then it begins listening in the background.

Say:

“Jarvis” → pause → give your command.

🗣️ Example Voice Commands
🌍 Maps & Directions

“Jarvis show me Taj Mahal in map”

“Jarvis open Ahmedabad in map”

“Jarvis show me direction from Surat to Pune in map”

🌐 General Websites

“Jarvis open Google”

“Jarvis open YouTube”

“Jarvis open Instagram”

💬 AI Answers

“Jarvis, what is artificial intelligence?”

“Jarvis, tell me a joke.”

🧠 How It Works
🎧 Listening

Uses speech_recognition to capture mic audio

Uses adjustable thresholds for faster response (pause_threshold, non_speaking_duration)

Wake-word detection triggers the command listener

🤖 AI Brain (Gemini)

Gemini responds to general questions using:

client.models.generate_content(model="gemini-2.5-flash", ...)


A system_instruction guides the behavior (short answers, etc.)

🔊 Speaking

Converts AI text → speech with gTTS

Plays output via pygame.mixer

🌐 Maps

Parses the command and opens Google Maps URLs:

https://www.google.com/maps/place/<location>
https://www.google.com/maps/dir/<from>/<to>

🛠️ Recommended Improvements

You can extend Jarvis by adding:

Offline speech recognition (Vosk + webrtcvad)

Wake-word engine (Picovoice Porcupine)

Weather API integration

Music player integration

Email/SMS automation

If you want help adding any of these, ask!

📁 Project Structure (typical)
project/
│─ main.py
│─ googleAI-key.txt      # your key (ignored in git)
│─ command.mp3           # TTS output (ignored)
│─ README.md
│─ requirements.txt

⚠️ Important Notes

Do not commit your API key — keep googleAI-key.txt private.

Gemini models do not verify the web automatically.
For accurate real-time facts (presidents, stock, news), add a web-scraping verification step.

Microphone sensitivity may require tuning via:

recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.6
recognizer.non_speaking_duration = 0.2

🧑‍💻 Contributing

Pull requests are welcome!
You may contribute fixes for:

Faster recognition

More built-in commands

Better verification for current-events queries

Additional integrations (Home automation, Spotify, WhatsApp API, etc.)

📜 License

MIT License