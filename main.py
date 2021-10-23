import os

os.system("pip install aiohttp==3.7.4.post0")
os.system("pip install astroid==2.4.2")
os.system("pip install pygame==2.0.2")
os.system("pip install async-timeout==3.0.1 ")
os.system("pip install attrs==20.3.0")
os.system("pip install backcall==0.2.0")
os.system("pip install beautifulsoup4==4.9.3")   
os.system("pip install cats==0.2.0")
os.system("pip install certifi==2020.12.5")
os.system("pip install chardet==4.0.0")
os.system("pip install click==8.0.1")
os.system("pip install colorama==0.4.4")
os.system("pip install config==0.5.0.post0  ")   
os.system("pip install decorator==5.0.7 ")   
os.system("pip install discord==1.0.1")
os.system("pip install discord.py==1.6.0")     
os.system("pip install docopt==0.6.2")
os.system("pip install gTTS==2.2.3")
os.system("pip install idna==2.10")
os.system("pip install install==1.3.4")
os.system("pip install ipykernel==5.5.3 ")       
os.system("pip install ipython==7.22.0")
os.system("pip install ipython-genutils==0.2.0 ")
os.system("pip install isort==5.7.0")
os.system("pip install jedi==0.18.0")
os.system("pip install Js2Py==0.71")
os.system("pip install jupyter-client==6.1.12")  
os.system("pip install jupyter-core==4.7.1   ")  
os.system("pip install lazy-object-proxy==1.4.3")
os.system("pip install mccabe==0.6.1")
os.system("pip install multidict==5.1.0")
os.system("pip install newsapi==0.1.1")
os.system("pip install newsapi-python==0.2.6")
os.system("pip install numpy==1.19.5")
os.system("pip install packaging==21.0")
os.system("pip install pandas==1.2.4")
os.system("pip install parso==0.8.2")
os.system("pip install pickleshare==0.7.5 ")     
os.system("pip install pipwin==0.5.1")
os.system("pip install playsound==1.3.0  ")      
os.system("pip install praw==7.2.0")
os.system("pip install prawcore==2.0.0")
os.system("pip install prompt-toolkit==3.0.18")
os.system("pip install Pygments==2.8.1")
os.system("pip install pyjsparser==2.7.1")
os.system("pip install pylint==2.6.0")
os.system("pip install pyparsing==2.4.7")
os.system("pip install PyPrind==2.11.3")
os.system("pip install pySmartDL==1.3.4")
os.system("pip install python-dateutil==2.8.1")
os.system("pip install pytz==2021.1")
os.system("pip install pywhatkit==3.9")
os.system("pip install pywin32==300")
os.system("pip install pyzmq==22.0.3")
os.system("pip install random-cat==1.0.1")
os.system("pip install requests==2.25.1")
os.system("pip install six==1.15.0")
os.system("pip install soupsieve==2.2.1")
os.system("pip install SpeechRecognition==3.8.1")
os.system("pip install speedtest-cli==2.1.2")
os.system("pip install toml==0.10.2")
os.system("pip install tornado==6.1")
os.system("pip install traitlets==5.0.5")
os.system("pip install typing-extensions==3.7.4.3")
os.system("pip install tzdata==2021.2")
os.system("pip install tzlocal==3.0")
os.system("pip install update-checker==0.18.0")
os.system("pip install urllib3==1.26.4")
os.system("pip install wcwidth==0.2.5")
os.system("pip install websocket-client==0.58.0")
os.system("pip install wikipedia==1.4.0")
os.system("pip install wrapt==1.12.1")
os.system("pip install yarl==1.6.3")
os.system("pip install requests==2.25.1")
os.system("pip install bs4==0.0.1")
os.system("pip install randfacts~=0.12.0")
os.system("pip install newsapi~=0.1.1")
os.system("pip install quote~=2.0.4")
os.system("pip install psutil")
os.system("pip install math")









import datetime
import json

import time
import weakref
import webbrowser
import requests
import base64
import pyttsx3
import playsound  # pip install playsound
import requests
import speech_recognition as sr  # pip install SpeechRecognition
from bs4 import BeautifulSoup
from gtts import gTTS  # pip install gTTS
import pyaudio  # pip install PyAudio
import speedtest  # for speedtest application
import pygame
import pywhatkit  # Whatsapp messaging
import psutil,math   #pip ionstall math
pygame.mixer.init()
pygame.init()


from newsapi import NewsApiClient  # for latest news api
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

# for playing music
def playmusic(): 
    # Here you can provide the mp3 file name.
    pygame.mixer.music.load("Tobu  Itro  Sunburst NCS Release.mp3")
    pygame.mixer.music.play()

# To stop the music
def stopmusic():
    pygame.mixer.music.stop()


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

def movie():
    page= requests.get('https://www.imdb.com/chart/top/')  #webscrapped imdb's top charts
    soup= BeautifulSoup(page.content, 'html.parser')
    links= soup.select("table tbody tr td.titleColumn a")  
    first10= links[:10]     
    for anchor in first10:
        print(anchor.text)
        speak(anchor.text)
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])      

def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    return final_res
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

    elif 'business quote' in query or 'say about business' in query:
        response=requests.get("https://efflux.herokuapp.com/business")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        print(quote)
        speak(quote)
    elif 'love quote' in query or 'say about love' in query:
        response=requests.get("https://efflux.herokuapp.com/love")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        print(quote)
        speak(quote)
    elif 'hustle quote' in query :
        response=requests.get("https://efflux.herokuapp.com/hustle")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        print(quote)
        speak(quote)
    elif 'life quote' in query or 'say about life' in query:
        response=requests.get("https://efflux.herokuapp.com/life")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        print(quote)
        speak(quote)
    elif 'friendship quote' in query or 'say about friendship' in query:
        response=requests.get("https://efflux.herokuapp.com/friendship")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        print(quote)
        speak(quote)
    elif 'war quote' in query or 'say about war' in query:
        response=requests.get("https://efflux.herokuapp.com/war")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        print(quote)
        speak(quote)
    elif 'game quote' in query or 'gaming quote' in query :
        response=requests.get("https://videogame-quotes-api.herokuapp.com/quotes")
        json_data=json.loads(response.text)
        quote =json_data['quote'] + " from "+json_data["game"]
        print(quote)
        speak(quote)

    elif "internet" in query and "speed" in query:
            speak("Wait for while...")
            st = speedtest.Speedtest()
            up = round(st.upload() / 10 ** 6, 2)
            down = round(st.download() / 10 ** 6, 2)
            print(f"Download Speed is {down} MB/s")
            speak(f"Download Speed is {down} MB per Sceond")
            print(f"Upload Speed is {up} MB/s")
            speak(f"Upload Speed is {up} Mb per Sceond")

    elif "suggest me movies" in query:
        speak("I scoured the internet and found the top 10 films according to imdb")
        print(f"I scoured the internet and found the top 10 films according to imdb")
        movie()
        time.sleep(0.2)     
        speak("now redirecting you to imdb site you can check more reviews there")
        webbrowser.open("https://www.imdb.com/chart/top/")

    elif "play music" in query:
        playmusic()
    elif "stop music" in query:
        stopmusic()

    elif 'fact' in query or 'facts' in query:
        get_facts()
    elif 'quote' in query:
        get_quote()
        # whatsapp messaging
    elif "message" in query:
        hr, min = datetime.datetime.now().hour, datetime.datetime.now().minute
        phone = credentials.contacts
        speak("whom did you want to send message")
        user = get_audio()
        speak("What is message")
        msg = get_audio()
        id = False
        for i in phone.keys():
            if i in user:
                user = i
                id = True
                break
        if id:
            speak(f"sending {msg} to {user}")
            pywhatkit.sendwhatmsg(f"{phone[user]}", f"{msg}", hr, min + 2)
        else:
            speak(f"We don't have {user} phone no.")
        # Exit the program
    elif "no thanks" in query or "exit" in query or "close" in query :
        speak("Thanks For using Me,Have a nice day")
        exit(0)
    elif "sleep" in query or "wait" in query:
        time.sleep(3)
    
    elif "system" in query:
        sys_info = system_stats()
        print(sys_info)
        speak(sys_info)

    else:
        speak("there is problem with command ,please say again..")
        continue
