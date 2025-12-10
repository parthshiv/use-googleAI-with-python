import speech_recognition as sr
import webbrowser
from gtts import gTTS #Google text-to-speech module
import os
import pygame # this module helps to play mp3
from google import genai
from google.genai import types

# use key to activate googleAI API
with open("googleAI-key.txt","r") as k:
    key = k.read()

client = genai.Client(api_key=key)
recognizer = sr.Recognizer()

# Tuning params
recognizer.dynamic_energy_threshold = False   # keep fixed energy
recognizer.energy_threshold = 300             # reduce/increase per your mic
recognizer.pause_threshold = 0.6
recognizer.non_speaking_duration = 0.2
# recognizer.phrase_time_limit = 3

def speak(text):
    tts = gTTS(text) #generates speech to text
    tts.save("command.mp3") #convert our speech into mp3 and save on system

    pygame.init()
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("command.mp3")
    pygame.mixer.music.play()
    
    # below while loop is important. checks if music is currently playing through the Pygame mixer's music module. It returns True if music is playing and False otherwise. This code creates a loop that effectively waits for a music track to finish playing. While the music is playing, the loop continuously checks its status
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10) # Adjust tick rate as needed

    pygame.mixer.music.unload() #it will release the file from system make it free, otherwise delete wont work
    os.remove("command.mp3") #will delete the file from system

def processCommand(c):
    ToDo = c.lower()

    if "open google" in ToDo:
        speak("Opening google")
        webbrowser.open("https://google.com")
    
    elif "show me direction" in ToDo and "from" in ToDo and "to" in ToDo:
        # Extract locations
        try:
            part = ToDo.split("show me direction")[1].strip()
            from_loc = part.split("from")[1].split("to")[0].strip()
            to_loc = part.split("to")[1].strip()
            speak(f"Opening directions from {from_loc} to {to_loc}...")
            # Build Google Maps URL
            url = f"https://www.google.com/maps/dir/{from_loc}/{to_loc}"
            webbrowser.open(url)
            
        except Exception as e:
            speak("Sorry, I couldn't understand the locations.")
    
    elif "show me" in ToDo and "in map"  in ToDo:
        try:
            
            place = ToDo.split("show me")[1].split("in map")[0].strip()            
            speak(f"Opening location: {place}")
            url = f"https://www.google.com/maps/place/{place}"        
            webbrowser.open(url)
            
        except Exception as e:
            speak("Sorry, I couldn't understand the locations.")
            
    elif "open youtube" in ToDo:
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open instagram" in ToDo:
        speak("Opening instagram")
        webbrowser.open("https://instagram.com")
    elif "open facebook" in ToDo:
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")

    else:
        speak("okay, wait a moment")
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=types.Part.from_text(text=c),
            config=types.GenerateContentConfig(
                system_instruction="Answer all outputs very shortly in 1 line only. For political/current queries you should verify online before responding.",
                temperature=0,
                top_p=0.95,
                top_k=20,
            ),
        )
        speak(response.text)

if __name__ == "__main__":
    speak("initializing Jarvis....")
    while True:
        
        with sr.Microphone() as source:
            print("Listening....")
            try:
                
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)   
                
                if "jarvis" in word.lower() or "hey jarvis" in word.lower() or "hello jarvis" in word.lower():
                    speak("Yaa?")
                    print("Jarvis Active!!!!") 
                    with sr.Microphone() as source:    
                        recognizer.adjust_for_ambient_noise(source, duration=1) 
                        doCommand = recognizer.listen(source, timeout=5, phrase_time_limit=1)
                        cmdTextFormat = recognizer.recognize_google(doCommand)                        
                        processCommand(cmdTextFormat)

            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
                continue # Continue to the next iteration of the loop

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
