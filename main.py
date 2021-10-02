import os
import time
import playsound  # pip install playsound
import speech_recognition as sr  # pip install speech_recognition
from gtts import gTTS  # pip install gTTS
import pyaudio  # pip install pyaudio
import datetime
from newsapi import NewsApiClient  # for latest news api
import credentials


# function to accept audio input from user#

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said=r.recognize_google(audio)
            print(said)
            
        except Exception as e:
            print("Exception: "+str(e))
            
    return said
#get_audio()


# function to convert text_to_speech#

def speak(text):
    tts = gTTS(text=text, lang="en-in")
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


# function for News
def news():
    # for latest news
    newsapi = NewsApiClient(api_key='{}'.format(credentials.newsapikey))
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(country='in')
    ranks = ["First", 'Sceond', 'Third', 'Fourth', 'Fifth']
    for i in range(5):
        # first five news
        print(f"{ranks[i]} News : {top_headlines['articles'][i]['title']}")
        speak(f"{ranks[i]} News : {top_headlines['articles'][i]['title']}".replace(" - ", "news by"))


# Voice_assistant skills#

time.sleep(2)
speak("Hi what can i do for you?")
while True:
    query = get_audio().lower()
    if 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    # add more functinalities below this:
    elif 'news' in query:
        news()
    else:
        break
