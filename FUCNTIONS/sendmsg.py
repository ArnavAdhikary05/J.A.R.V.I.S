import pywhatkit
from ENGINS.TTS.stream_elements_api import speak
from FUCNTIONS.time import * 
def sendMessage(message, recipient):
    #if recipient == "mother":
    pywhatkit.sendwhatmsg("+918981254062",message,current_hour,current_minute+1)
    speak("message sent")