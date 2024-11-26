import threading
import os
import pyautogui
import time

def run_gui():
    os.system("python eel_window.py")

def run_jarvis():
    os.system("python main.py")

if __name__ == "__main__":
    gui_thread = threading.Thread(target=run_gui, daemon=True)
    jarvis_thread = threading.Thread(target=run_jarvis, daemon=True)

    gui_thread.start()
    jarvis_thread.start()
    # Simulate pressing Windows + Right Arrow
    time.sleep(2)
    pyautogui.hotkey('win', 'right')
    time.sleep(1)
    pyautogui.press('enter')

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down...")



