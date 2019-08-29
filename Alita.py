import os
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()
sound = engine.getProperty('voices')
Ch_gender = engine.setProperty('voice', sound[1].id)

def speaks(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommands():
    #it takes user's voice as an input and return output in a string
    recog = sr.Recognizer()
    with sr.Microphone()as source:
        speaks("I am listening sir! Go ahead..")
        recog.pause_threshold = 1
        aud = recog.listen(source)
    try:

     print("Recognizing...")
     query = recog.recognize_google(aud,language='en-US')
     print(f"user said:{query}\n")

    except Exception as e:
        speaks("Sorry sir! I am unable to recognize your words. Please say that again!")
        # return "none"
    return query

if __name__ == '__main__':
    while True:
        query = takecommands().lower() # lower() for lowercase letter

        if 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
       
        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open wikipedia' in query:
            speaks("Searching Wikipedia Sir...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=1)
            speaks("According to wikipedia sir")
            print(result)
            speaks(result)

