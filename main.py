import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
import pygame
from openai import OpenAI
from gtts import gTTS
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "b9a86bb49dfa43e7a653aeaf62add163"
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"

def speak_old (text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.runAndWait()
    engine.say(text)
    engine.stop()  #important

def speak (text) :
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Loadthe mp3 file
    pygame.mixer.music.load ('temp.mp3')

    # Play the mp3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload ()
    os.remove ("temp.mp3")

def aiProcess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google CLoud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message

def processCommand(c):
    if "open google" in c.lower():
        speak ("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak ("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        speak ("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        speak ("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        speak (f"playing {song}")
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(url)
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles',[])

            # Print the headlines
            for article in articles:
                speak (article['title'])

    else :
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak (output)
        
                

if __name__ == "__main__":
    speak ("Initializing Jarvis....")

    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        # recognize speech using Sphinx
        print ("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)

            if (word.lower() == "jarvis"):
                time.sleep(0.5)  #important
                speak ("What Happened?")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated !")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))