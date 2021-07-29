import smtplib
import webbrowser
import speech_recognition as sr
import datetime
import os
import pyttsx3
import wikipedia
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
email_id = {'jigar rajeshkumar': 'jigarsirt15@gmail.com'}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am Jarvis , Please tell me how may I help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    else:
        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jigarsirt15@gmail.com','Rajeshkumar15@')
    server.sendmail('jigarsirt15@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Desk\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time is {strTime}")
        elif 'send email' in query:
            try:
                speak("What should I say ")
                content = takeCommand()
                to = takeCommand()
                if to == email_id:
                    sendEmail(to, content)
                    speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir ,I am not able to send this email...")
