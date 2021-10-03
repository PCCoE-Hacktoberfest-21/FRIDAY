import datetime
import json
import os
import time

import playsound  # pip install playsound
import requests
import speech_recognition as sr  # pip install SpeechRecognition
from bs4 import BeautifulSoup
from gtts import gTTS  # pip install gTTS
import pyaudio        #pip install PyAudio
# function to accept audio input from user
# get_audio()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said


# function to return joke from api
def get_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    json_data = json.loads(response.text)
    joke = json_data['joke']
    return joke


# function to convert text_to_speech

def speak(text):
    tts = gTTS(text=text, lang="en-in")
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def check_command_is_for_covid_cases(command):
    country = get_country(command).capitalize()
    cases = get_covid_cases(country)
    speak(f"The current active cases in {country} are {cases}")


def get_country(command):
    country = command.split()[-1]
    if country == "?":
        country = command.split()[-2]
    return country


def get_covid_cases(country):
    totalActiveCases = 0
    response = requests.get('https://api.covid19api.com/live/country/' + country + '/status/confirmed').json()
    for data in response:
        totalActiveCases += data.get('Active')
    return totalActiveCases


# Voice_assistant skills#

time.sleep(2)
speak("Hi what can i do for you?")

last_query = None

while True:
    query = get_audio().lower()
    if 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'active cases of covid-19' in query:
        check_command_is_for_covid_cases(query)

    elif 'joke' in query:
        speak(get_joke())

    if last_query:
        if last_query == 'open notepad':
            with open('notepad.txt', 'w+') as file:
                file.write(query)

    elif 'open notepad' in query:
        last_query = 'open notepad'

    elif 'weather' in query:
        speak("Please tell your city name?")
        city = get_audio().lower()
        # creating url and requests instance
        url = "https://www.google.com/search?q=" + "weather" + city
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
