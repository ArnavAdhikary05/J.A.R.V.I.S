from IMPORTS import *
from datetime import datetime
def wish():
    ch = (1,2,3,4,5) # You can choose any number of songs (I have only choosen 3)
    bh = random.choice(ch)
    if bh==1:
        speak("Welcome back, SIR")
    elif bh==2:
        speak("Hello, SIR")
    elif bh==3:
        speak("Hi, SIR")
    elif bh==4:
        speak("Hey, SIR")
    elif bh==5:
        speak("Hi there, SIR")
    elif bh==6:
        GreetMe()
    
def me():
    ch1 = (1,2,3,4,5,6,7,8,9,10) # You can choose any number of songs (I have only choosen 10)
    ch2 = random.choice(ch1)
    if ch2 == 1: 
        speak("Jarvis here, ready to assist.")
    elif ch2 == 2: 
        speak("I am Jarvis, at your service.")
    elif ch2 == 3: 
        speak("This is Jarvis, how can I help you today?")
    elif ch2 == 4: 
        speak("Jarvis, standing by.")
    elif ch2 == 5: 
        speak("I’m Jarvis, your trusted assistant.")
    elif ch2 == 6: 
        speak("Hello, I’m Jarvis. Let’s get started.")
    elif ch2 == 7: 
        speak("Jarvis reporting for duty.")
    elif ch2 == 8: 
        speak("I am Jarvis, programmed for your convenience.")
    elif ch2 == 9: 
        speak("This is Jarvis, ready to tackle any task.")
    elif ch2 == 10: 
        speak("I’m Jarvis, here to make your life easier.")
    
