import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
from tkinter import *

Faizan_root = Tk()
Faizan_root.geometry("300x400")
Faizan_root.title("JARVIS AI by Faizan Jallani")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

WAKE = "hey jarvis"
SERVICE = authenticate_google()
print("Start")

while True:
    print("Listening...")
    text = get_audio()

if text.count(WAKE) > 0:
    speak("I am ready")
    text = get_audio()


def wishMe():
    hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    speak("Good Morning!")

elif hour>=12 and hour<18:
    speak("Good Afternoon!")

else:
    speak("Good Evening!")

speak("I am JARVIS. How may I help you Sir?")

def takeCommand():
    r = sr.Recognizer()
with sr.Microphone () as source:
    print("Listening...")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")

except Exception as e:
    # print(e)
    speak("Say that again please...")
    return"None"
return query

if _name_ == '_main_':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2 )
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/", new=2)
            speak("Enjoy")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/", new=2)

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/", new=2)

        elif 'play music' in query:
            music_dir = 'F:\\songs\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Faizan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/", new=2)

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/faizangujjar01/", new=2)
            speak("Have a look sir")

        elif 'are you there' in query:
            stMsgs = ['At you service, Sir']
            speak(stMsgs)

        elif 'shutdown the PC' in query:
            choice = input("Please confirm to shutdown the pc (y or n)")
            if choice == 'n':
                exit()
            else:
                os.system("shutdown /s /t 1")

        elif 'exit' in query:
            sys.exit(speak("Ok sir, Take Care."))

        test2.py    

Faizan_root.mainloop()