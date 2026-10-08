# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests

# recognizer = sr.Recognizer()
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 160)
# newsapi = "82219a5c3a58413797610e56ce2c39f7"

# def speak(text):
#     print(f"Speaking: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     c = c.lower()
#     print(f"Processing command: {c}")

#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#         speak("Opening google")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#         speak("Opening youtube")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#         speak("Opening facebook")
#     elif "news" in c.lower():
#         r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=82219a5c3a58413797610e56ce2c39f7")
#         if r.status_code == 200:
#             data = r.json()
#             articles = data.get("articles", [])
            
#             for article in articles:
#                 speak(article['title'])


#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         if link:
#             webbrowser.open(link)
#             speak(f"Playing {song}")
#         else:
#             speak(f"Sorry, I don't have {song} in the library.")
#     else:
#         speak("Sorry, I didn't understand that command.")

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     r = sr.Recognizer()
#     r.energy_threshold = 250
#     r.dynamic_energy_threshold = True
#     r.dynamic_energy_adjustment_damping = 0.15

#     mic = sr.Microphone(device_index=1)

#     while True:
#         try:
#             with mic as source:
#                print("\nListening for 'Jarvis'...")
#                r.adjust_for_ambient_noise(source, duration = 1.0)
#                audio = r.listen(source, timeout = 8, phrase_time_limit = 4)

#             word = r.recognize_google(audio, language="en-IN")
#             print(f"You said: {word}")

#             if "jarvis" in word.lower():
#                 print("wake word detected - saying 'Ya'")
#                 speak("Ya")
#                 speak("What can I do for you?")

#                 with mic as source:
#                     print("Listening for command...")
#                     r.adjust_for_ambient_noise(source, duration = 0.8)
#                     audio = r.listen(source, timeout = 7, phrase_time_limit = 5)

#                 command = r.recognize_google(audio, language="en-IN")
#                 print(f"Command: {command}")
#                 processCommand(command)

#         except sr.UnknownValueError:
#             pass
#         except sr.RequestError as e:
#             print(f"Google error: {e}")
#         except Exception as e:
#             print(f"Error: {type(e).__name__}: {e}")
           

