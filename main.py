from IMPORTS import *

battery = psutil.sensors_battery()
percentage = battery.percent

def objdct():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Load the YOLO model
    # model = YOLO("FUCNTIONS\yolov8l.pt")
    model = YOLO("FUCNTIONS\yolov8n.pt")

    start_time = time.time()
    recognized_objects = []  # List to store recognized objects

    while True:
        # Read frame from the camera
        success, img = cap.read()
        
        # Process the image with the YOLO model
        results = model(img, stream=True)
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Check the length of box.xyxy
                if len(box.xyxy[0]) == 4:
                    # Extract bounding box coordinates
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    
                    # Get class ID and name
                    class_id = int(box.cls[0])
                    class_name = model.names[class_id]
                    
                    # Draw rectangle and put text
                    w, h = x2 - x1, y2 - y1
                    cvzone.cornerRect(img, (x1, y1, w, h))
                    cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

                    # Add recognized object to the list
                    recognized_objects.append(class_name)

        # Display the image
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        # Check if 5 seconds have passed
        current_time = time.time()
        if current_time - start_time >= 5:
            break

    # Count occurrences of each recognized object
    object_count = Counter(recognized_objects)

    # Get the four most common objects
    most_common_objects = object_count.most_common(4)

    # Print the four most recognized objects in series
    print("Four most recognized objects:")
    speak("I can see")
    for obj, _ in most_common_objects:  # Ignore the count
        print(obj)
        speak(obj)

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()
def TaskExecutor():
        print('J.A.R.V.I.S')
        wish()
        me()
        
        #this will make jarvis listen to us
        while True:
            
            query = takeCommand().lower().strip()
            #this makes jarvis open any website.
            sites = [["wikipedia", "https://www.wikipedia.org/"],["google","https://www.google.com/"],["facebook","https://www.facebook.com/"],["instagram","https://www.instagram.com"]]
            for site in sites:
                if f"Open {site[0]}".lower() in query:
                    speak(f"Opening {site[0]}...")
                    webbrowser.open(site[1])

            if "what can you see" in query:
                objdct()

            elif "wake up" in query:
                from FUCNTIONS.GreetMe import greetMe
                greetMe()
                speak("Please tell me, How can I help you ?")

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can me call anytime")
                        break 

            elif "goodbye" in query:
                speak("good bye sir!")
                exit()
            elif "current time" in query:
                strTime = datetime.now().strftime("%I:%M %p")
                speak(f"Sir, It's {strTime}") 
            
            elif "weather" in query:
                search = "temperature in kolkata"
                url = f"https://www.google.com/search?q={search}"
                r  = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current{search} is {temp}")
            
            elif "alarm" in query:
                print("Sir, please tell me the time to set alarm! as example, set alarm to 5:30 am")
                speak("Sir, please tell me the time to set alarm! as example, set alarm to 5:30 am")
                tt = takeCommand().lower()
                tt = tt.replace("set alarm to ","")
                tt = tt.replace(".","")
                tt = tt.upper()
                alarm(tt)

            elif "open" in query:
                query = query.replace("open","")
                query = query.replace("jarvis","")
                open(query,match_closest=True)
                speak("Opening"+query)
                
            elif "close" in query:
                query = query.replace("close","")
                query = query.replace("jarvis","")
                close(query,match_closest=True)
                speak("Closing"+query)

            elif "type" in query:
                query = query.replace("type","")
                pyautogui.press("/")
                pyautogui.write(query)

            # elif "open" in query:
            #     from FUCNTIONS.Dictapp import openappweb
            #     openappweb(query)
            
            # elif "close" in query:
            #     from FUCNTIONS.Dictapp import closeappweb
            #     closeappweb(query)
            
            elif "google" in query:
                from FUCNTIONS.SearchNow import searchGoogle
                searchGoogle(query)
            
            elif "on youtube".lower() in query.lower():
                from FUCNTIONS.SearchFromYt import SearchYt
                SearchYt(query)

            elif "song please".lower() in query.lower() or "play some song".lower() in query.lower() or "could you play some song".lower() in query.lower():
                speak("which song should i play, sir...")
                song = takeCommand()
                webbrowser.open(f"https://open.spotify.com/search/{song}")
                sleep(13)
                # pyautogui.click(x=1087, y=385)
                pyautogui.click(x=1003, y=419)
                speak("playing"+ song)
            #spotify
            elif "play".lower() and "song".lower() in query.lower() or "could you play".lower() in query.lower() or "please play".lower() in query.lower():
                speak("OK! here you go !")
                query = query.replace("play", "")
                query = query.replace("the", "")
                query = query.replace("song", "")
                query = query.replace("could you play", "")
                query = query.replace("please play", "")
                webbrowser.open(f"https://open.spotify.com/search/{query}")
                sleep(13)
                pyautogui.click(x=1087, y=385)
                speak("playing"+ query)

            elif (percentage<20):
                speak("Your battery is 20%, please plug the charger")
            elif (percentage==100):
                speak("Your battery is fully charged, Unplug the charger")


            # elif "volume up" in query:
            #     from keyboard import volumeup # type: ignore
            #     speak("Turning volume up,sir")
            #     volumeup()
            # elif "volume down" in query:
            #     from keyboard import volumedown # type: ignore
            #     speak("Turning volume down, sir")
            #     volumedown()
            elif "stop" in query:
                press("k")
                speak("video paused")
            
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

            elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                        img = Image.open("ss.jpg")
                        # Display the image
                        speak("screenshot taken, saved as ss.jpg")
                        img.show()
                        
            elif "take a picture" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")
            elif "shutdown the system" in query:
                speak("Okay, Shuting down")
                os.system("shutdown /s /t 5")
            elif "restart the system" in query:
                speak("Okay, restarting your computer")
                os.system("shutdown /r /t 5")
            elif "sleep" and "system" in query:
                speak("Okay, Entering sleeping mode?")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            
            elif "send a message" in query:
                speak("What is the message you want to send?")
                query = takeCommand().lower()
                speak("To whom you want to send the message?")
                recipient = takeCommand().lower()
                print("sending message to %s" % recipient)
                sendMessage(query,recipient)

            
            #will tell the date
            elif "the date".lower() in query.lower():
                today = date.today()
                d4 = today.strftime("%b-%d-%Y")         
                speak(f"The date is {d4}")
            
            elif "wikipedia" in query:
                from FUCNTIONS.SearchNow import searchWikipedia
                searchWikipedia(query)

            elif "news" in query:
                from FUCNTIONS.NewsRead import latestnews
                latestnews()
            
            elif "start" in query:
                press("k")
                speak("video played")
            elif "mute" in query:
                press("m")  # YouTube mute toggle
                speak("video muted")

            elif "tired" in query:
                speak("Playing your favourite songs, sir")
                a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                b = random.choice(a)
                if b==1:
                    webbrowser.open("https://www.youtube.com/watch?v=rtTI1rh9U5M&t=314s")
                elif b==2:
                    webbrowser.open("https://www.youtube.com/watch?v=39uMLYTh40Q&t=326s")
                elif b==3:
                    webbrowser.open("https://www.youtube.com/watch?v=IWmmv7T-D7U")
            

            elif "generate a image" in query:
                from FUCNTIONS.image_gen import img_gen
                img_gen(query, "genimage.png")
                img = Image.open("genimage.png")
                # Display the image
                img.show()
            

            elif "emotion detection" in query:
                speak("press q to stop the program")
                import FUCNTIONS.emotiondetect 
                subprocess.run(["python", "emotiondetect.py"])
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                print(f"Your IP address is {ip}")
                speak(f"Your IP address is {ip}")
            elif "virtual" and "mouse" in query:
                speak("Virtual mouse is activated")
                mcontrol()
            elif " " in query:
                answer = generate(query, web_access=True, stream=True)
                speak(answer) 
            
            else:
                continue
            
#TaskExecutor()

if __name__ == '__main__':
    from main import TaskExecutor

    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 2 #number of persons you want to Recognize


    names = ['','Arnav','elon']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
            
            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak(f"Face recognized as {id}".format())
                cv2.waitKey(1000)  # wait for 1 seconds before closing the window
                cv2.destroyAllWindows()
                TaskExecutor()
                
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("Face not recognized")

            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()
