import cv2
import numpy as np
import dlib
from imutils import face_utils
import pygame
import os

# Set the DISPLAY environment variable to :0
os.environ["DISPLAY"] = ":0"
# Set the custom audio device to the built-in audio output (bcm2835 Headphones)
os.environ["AUDIODEV"] = "hw:1,0"

# Now you can run your code that requires the DISPLAY environment variable


pygame.init()
pygame.mixer.music.load("/home/pi/fp/beep.mp3")
pygame.mixer.music.play()
cap = cv2.VideoCapture(0)
# Set resolution to 720p
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# Set frame rate to 30 FPS
cap.set(cv2.CAP_PROP_FPS,30)

#Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/pi/fp/shape_predictor_68_face_landmarks.dat")

sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# Initialize pygame
#pygame.init()

# Load audio files
#drowsy_sound = pygame.mixer.Sound("wakeup.wav") # additional sound output for drowsy
pygame.mixer.music.load("/home/pi/fp/wakeup3.mp3")

def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    
    if ratio > 0.25:
        return 2
    elif 0.21 < ratio <= 0.25:
        return 1
    else:
        return 0

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    face_frame = None  # Initialize face_frame to None
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 9:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                #pygame.time.wait(int(pygame.mixer.music.get_length()*1000))
        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
                #drowsy_sound.play() # To play other sound for drowsy
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "Active :)"
                color = (0, 255, 0)
        	
        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    if face_frame is not None and face_frame.shape[0] > 0 and face_frame.shape[1] > 0:  # Add this additional check
    	cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
