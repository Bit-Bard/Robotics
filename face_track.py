import cv2
import time
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000, pin_factory=factory)
tilt = Servo(27, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000, pin_factory=factory)

pan.mid()
tilt.mid()
time.sleep(1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

Kp = 0.003
pan_pos = 0
tilt_pos = 0

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    h, w = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        x, y, fw, fh = faces[0]
        cx = x + fw//2
        cy = y + fh//2

        error_x = cx - w//2
        error_y = cy - h//2

        pan_pos -= Kp * error_x
        tilt_pos += Kp * error_y

        pan_pos = max(-1, min(1, pan_pos))
        tilt_pos = max(-1, min(1, tilt_pos))

        pan.value = pan_pos
        tilt.value = tilt_pos

    time.sleep(0.03)
