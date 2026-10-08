import dotenv
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from dotenv import load_dotenv
import os
load_dotenv()

def get_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    return engine

def speak(text):
    print(f"Speaking: {text}")
    try:
        engine = get_engine()         
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

def processCommand(c):
    c = c.lower().strip()
    print(f"Processing command: {c}")
    
    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "news" in c:
        try:
            newsapi = os.getenv("NEWS_API_KEY")
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                for article in articles[:3]:   
                    speak(article['title'])
        except Exception as e:
            speak("Sorry, I couldn't fetch the news")
    elif c.startswith("play"):
        song = c.split("play")[-1].strip()   
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I don't have {song} in my library.")
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    r = sr.Recognizer()
    r.energy_threshold = 250
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    
    mic = sr.Microphone(device_index=1)   
    
    while True:
        try:
            with mic as source:
                print("\nListening for 'Jarvis'...")
                r.adjust_for_ambient_noise(source, duration=1.0)
                audio = r.listen(source, timeout=8, phrase_time_limit=4)
            
            word = r.recognize_google(audio, language="en-IN")
            print(f"You said: {word}")
            
            if "jarvis" in word.lower():
                print("Wake word detected")
                speak("Ya")
                speak("What can I do for you?")

                with mic as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source, duration=0.8)
                    audio = r.listen(source, timeout=7, phrase_time_limit=5)
                
                command = r.recognize_google(audio, language="en-IN")
                print(f"Command: {command}")
                processCommand(command)
                
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Google error: {e}")
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")