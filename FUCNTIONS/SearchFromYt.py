    
# importing the module
import pywhatkit
import speech_recognition as sr
import pyautogui
import time
import keyboard # type: ignore
from ENGINS.TTS.stream_elements_api import speak

        
# using Exception Handling
# to avoid exceptions
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening.....")
    r.pause_threshold = 1
    r.energy_threshold = 300
    audio = r.listen(source,0,4)
    #engine.say("I am listening")
    #engine.runAndWait()

def SearchYt(query):
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
            

    try:
        query = query.replace("play","")
        query = query.replace("on youtube","")
        
        # it plays a random YouTube
        # video of GeeksforGeeks
        pywhatkit.playonyt(query)
        # using the engine to speak
        # the output text
        speak("This is what i found..")
        keyboard.press('f')
        
        # printing the output text
        print("Playing...")
        keyboard.press('k')
        
        
    except:
        
        # printing the error message
        print("Network Error Occurred")
