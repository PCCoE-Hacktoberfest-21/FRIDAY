import os
import time
import playsound       #pip install playsound
import speech_recognition as sr   #pip install speech_recognition
from gtts import gTTS     #pip install gTTS
import pyaudio        #pip install pyaudio
import datetime   
import requests
from bs4 import BeautifulSoup


#function to accept audio input from user#

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
#get_audio()


#function to convert text_to_speech#

def speak(text):
    tts=gTTS(text=text,lang="en-in")
    filename="voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)



#Voice_assistant skills#

time.sleep(2)
speak("Hi what can i do for you?")

last_query = None

while True:
        query = get_audio().lower()
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # add more functinalities below this:
        if last_query:
            if last_query == 'open notepad':
                with open('notepad.txt','w+') as file:
                    file.write(query)

        elif 'open notepad' in query:
            last_query = 'open notepad'

        if 'weather' in query:
            speak("Please tell your city name?")
            city = get_audio().lower()
            # creating url and requests instance
            url = "https://www.google.com/search?q="+"weather"+city
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = str.split('\n')
            sky = data[1] 
            speak(f"Temperature for {city} today is {temp} °C")
            speak(f"And the sky will be {sky}")

        else:
            break
