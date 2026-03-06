import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import random
import sounddevice as sd
import soundfile as sf

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    duration = 5      # seconds
    fs = 44100        # sample rate

    try:
        print("Listening...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        sf.write("input.wav", recording, fs)

        with sr.AudioFile("input.wav") as source:
            audio = recognizer.record(source)

        command = recognizer.recognize_google(audio, language="en-in")
        print("You said:", command)
        return command.lower()

    except Exception as e:
        speak("Sorry, please say that again.")
        return ""

# Start assistant
greet()

while True:
    command = take_command()
    if command == "":
        continue

    if "time" in command:
        speak(datetime.datetime.now().strftime("The time is %H:%M"))

    elif "date" in command:
        speak(datetime.datetime.now().strftime("Today's date is %d %B %Y"))

    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        try:
            query = command.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("I couldn't find that on Wikipedia.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "play music" in command:
        music_path = "C:\\Users\\Yashaswini\\Music"  # change if needed
        songs = os.listdir(music_path)
        os.startfile(os.path.join(music_path, random.choice(songs)))
        speak("Playing music")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif any(word in command for word in ["exit", "bye", "stop", "quit"]):
        speak("Goodbye! Have a nice day.")
        break
    
