import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import time
import subprocess
import random
from openai import OpenAI

rate = 200

phrases = ["Je relache maintenant toutes les impulsions irréfléchies et destructrices",
           "Je me libère de la croyance que je serai submergé par l'anxiété",
           "Je me libère de toutes mes compulsions et addictions",
           "Je me libère du besoin de me consumer en essayant de satisfaire tous mes désirs",
           "Je me libère de la tenatavie de fuir les conséquences de mes actes",
           "Je me libère de la tentative de fuir les conséquences de mes actes"]

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        # speak("Hello,Good Evening")
        speak("Bonsoir Pascal")
        # speak(phrases[0])
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='fr-FR')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Je ne comprends pas, articule")
            return "None"
        return statement




if __name__=='__main__':
    wishMe()
    


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
        elif 'inspiration' in statement or 'aspiration' in statement:
            val = random.randint(0,len(phrases)-1)
            engine.setProperty('rate',150)
            speak(phrases[val])
            engine.setProperty('rate',rate)
        elif statement==0:
            continue