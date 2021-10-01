import os
import time
import playsound       #pip install playsound
import speech_recognition as sr   #pip install speech_recognition
from gtts import gTTS     #pip install gTTS
import pyaudio        #pip install pyaudio
import datetime   



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
while True:
        query = get_audio().lower()
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # add more functinalities below this:
        
        else:
            break
