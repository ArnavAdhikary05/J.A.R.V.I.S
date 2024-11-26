from ultralytics import YOLO
import cv2
import cvzone
import time
from collections import Counter
from ENGINS.TTS.stream_elements_api import speak

def objdct():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Load the YOLO model
    #model = YOLO("yolov8l.pt")
    model = YOLO("FUCNTIONS\yolov8l.pt")

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

objdct()