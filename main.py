import datetime
import json
import os
import time
import requests
import base64

import playsound  # pip install playsound
import requests
import speech_recognition as sr  # pip install SpeechRecognition
from bs4 import BeautifulSoup
from gtts import gTTS  # pip install gTTS
import pyaudio  # pip install PyAudio
import speedtest  # for speedtest application
import smtplib 
from email.message import EmailMessage 


# from newsapi import NewsApiClient  # for latest news api
import credentials

#if pyaudio installation is failed, try installing it with pywin
import randfacts as rf #pip install randfacts
from quote import quote

# function to accept audio input from user
# get_audio()
def get_audio():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said


# function to convert text_to_speech
def speak(text):
    tts = gTTS(text=text, lang="en-in")
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Voice_assistant skills#

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

# function to return joke from api
def get_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    json_data = json.loads(response.text)
    joke = json_data['joke']
    return joke


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

def get_trending_topics(trending_topics):
    consumer_key = os.getenv('consumer_key') #set consumer key using twitter developer account api in environment variables
    consumer_secret_key = os.environ.get('consumer_secret_key') #set consumer secret key using twitter developer account api in environment variables
    # Reformat the keys and encode them
    key_secret = '{}:{}'.format(consumer_key, consumer_secret_key).encode('ascii')
    # Transform from bytes to bytes that can be printed
    b64_encoded_key = base64.b64encode(key_secret)
    # Transform from bytes back into Unicode
    b64_encoded_key = b64_encoded_key.decode('ascii')
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']
    trend_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    trend_params = {
        'id': 2295411,  # set to 1 if you want global trending topics, currently set to WOEID of mumbai
    }
    trend_url = 'https://api.twitter.com/1.1/trends/place.json'
    trend_resp = requests.get(trend_url, headers=trend_headers, params=trend_params)
    tweet_data = trend_resp.json()
    for i in range(0, 5):
        tt = tweet_data[0]['trends'][i]['name']
        trending_topics.append(tt[1:])

# function to get meaning of a word
def get_meaning():
    speak("Please say the word you want to know meaning of")
    word = get_audio().lower()
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)
    json_data = json.loads(response.text)
    meaning = json_data[0]["meanings"][0]["definitions"][0]["definition"]
    return meaning

def get_facts():
    speak(rf.get_fact())

def get_quote():
    qt = quote(limit=1)
    for i in range(len(qt)):
        qt_say = qt[i]['quote'] + ' given by ' + qt[i]['author']
        speak(qt_say)


# function to send email
def send_email(sender, receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    email_id = 'xyz@gmail.com'
    password = 'xyz@123'
    server.login(email_id, password)

    email = EmailMessage()  # Create an instance
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()




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


    elif 'trending' in query:
        trending_topics = []
        get_trending_topics(trending_topics)
        for i in trending_topics:
            speak(i)

    elif 'meaning' in query:
        speak(get_meaning())
    
    elif 'news' in query:
        news()

    elif 'fact' or 'facts' in query:
        get_facts()

    elif "internet" in command and "speed" in command:
            speak("Wait for while...")
            st = speedtest.Speedtest()
            up = round(st.upload() / 10 ** 6, 2)
            down = round(st.download() / 10 ** 6, 2)
            print(f"Download Speed is {down} MB/s")
            speak(f"Download Speed is {down} MB per Sceond")
            print(f"Upload Speed is {up} MB/s")
            speak(f"Upload Speed is {up} Mb per Sceond")


    elif 'quote' in query:
        get_quote()
    
    elif 'send email' in query:
        sender = "xyz@gmail.com"
        receiver = "abc@gmail.com"
        subject = "send email"
        message = "Testing send email"
        send_email(sender, receiver, subject, message)

    else:
        break
