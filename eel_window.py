import eel  # type: ignore # Import the eel module for creating desktop applications with web technologies
import os  # Import the os module for interacting with the operating system

# Set the web folder and initial HTML file
eel.init('DESIGN')  # Initialize the eel module with the 'DESIGN' directory

# Use the os module to start Microsoft Edge in app mode with the specified URL
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# Start the Eel application with the specified HTML file and settings
# The mode is set to None, which means it won't try to open a browser
# The host is set to 'localhost'
# block is set to True, which means it will block and prevent the script from exiting immediately

eel.start('index.html', mode=None, host='localhost', block=True)
