from pyautogui import press ,hotkey
from ENGINS.TTS.stream_elements_api import speak
from ENGINS.STT.stt import takeCommand


query = takeCommand().lower().strip()
def click():

        if "stop" in query:
            press("k")
            speak("video paused")
        elif "start" in query:
            press("k")
            speak("video played")
        elif "mute" in query:
            press("m")  # YouTube mute toggle
            speak("video muted")
        elif "next" in query:
            hotkey('shift', 'n')
            speak("Playing next video")
        elif "volume up" in query:
            press("volumeup")
            speak("Turning volume up")
        elif "volume down" in query:
            press("volumedown")
            speak("Turning volume down")
        elif "previous" in query:
            hotkey('shift', 'p')
            speak("Playing previous video")

click()
            