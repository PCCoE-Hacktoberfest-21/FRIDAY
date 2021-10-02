import os
import time
import playsound       #pip install playsound
import speech_recognition as sr   #pip install SpeechRecognition
from gtts import gTTS     #pip install gTTS
import pyaudio        #pip install PyAudio
import datetime   
import requests
import json


#function to accept audio input from user
def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        
        try:
            said=r.recognize_google(audio)
            print(said)
            
        except Exception as e:
            print("Exception: "+str(e))
            
    return said

#function to return joke from api 
def get_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    json_data = json.loads(response.text)
    joke = json_data['joke']
    return joke

#function to convert text_to_speech
def speak(text):
    tts=gTTS(text=text,lang="en-in")
    filename="voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


#Voice_assistant skills
time.sleep(2)
speak("Hi what can i do for you?")

last_query = None

while True:
        query = get_audio().lower()
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # add more functionalities below this:

        elif 'joke' in query:
            speak(get_joke())

        if last_query:
            if last_query == 'open notepad':
                with open('notepad.txt','w+') as file:
                    file.write(query)

        elif 'open notepad' in query:
            last_query = 'open notepad'
        else:
            break
