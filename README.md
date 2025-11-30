# **AI-Powered Pan–Tilt Expression Tracking System (Raspberry Pi + OpenCV + Servos)**

## ** Introduction**

This project builds an **autonomous pan–tilt camera system** using a Raspberry Pi, OpenCV, and two micro-servos.
The system detects a human face in real time and **automatically rotates the camera** so that the face stays centered.
It also performs **expression/smile detection** using Haar Cascades.
This is a complete robotics + computer vision project designed for beginners and intermediate learners.

---

## **📦 Hardware Requirements**

| Component                                 | Description               |
| ----------------------------------------- | ------------------------- |
| **Raspberry Pi 3B+**                      | Main controller           |
| **Raspberry Pi Camera Module (V1 or V2)** | For live video feed       |
| **2x SG90 Micro Servo Motors**            | Pan and Tilt control      |
| **Pan–Tilt Bracket**                      | Holds the camera + servos |
| **Breadboard + Jumper Wires**             | For wiring                |
| **5V Power (from Pi Pin 2 or 4)**         | Servo power supply        |
| **GPIO Pins (e.g., GPIO 16 & 18)**        | Servo signal              |

---

## **🖥️ Software Requirements**

| Software                       | Purpose                     |
| ------------------------------ | --------------------------- |
| **Raspberry Pi OS (Bullseye)** | Operating system used       |
| **Python 3**                   | Programming                 |
| **OpenCV**                     | Face + expression detection |
| **GPIO Zero / RPi.GPIO**       | Servo control               |
| **libcamera**                  | Camera access pipeline      |

---

## **📁 Project Files Included**

| File                                  | Description                                      |
| ------------------------------------- | ------------------------------------------------ |
| `pan_tilt_expression_track.py`        | Main script (camera + detection + servo control) |
| `haarcascade_frontalface_default.xml` | Face detection model                             |
| `haarcascade_smile.xml`               | Smile detection model                            |

Folder structure example:

```
Robotics/
    pan_tilt/
        pan_tilt_expression_track.py
        haarcascade_frontalface_default.xml
        haarcascade_smile.xml
```

---

## **🔧 Setup Instructions**

### **1️⃣ Enable the Camera**

```
sudo raspi-config
```

Go to:
**Interface Options → Camera → Enable**

Reboot:

```
sudo reboot
```

---

### **2️⃣ Install Required Libraries**

```
sudo apt update
sudo apt install python3-opencv python3-pip -y
pip3 install RPi.GPIO
```

---

### **3️⃣ Clone or Copy This Repository**

```
mkdir ~/Robotics
cd ~/Robotics
git clone <your-repo-link>
cd pan_tilt
```

---

### **4️⃣ Wire the Servo Motors**

| Servo    | GPIO Pin | Power    |
| -------- | -------- | -------- |
| **Pan**  | GPIO 16  | 5V & GND |
| **Tilt** | GPIO 18  | 5V & GND |

⚠️ Both servos share the same 5V and GND from Raspberry Pi.

---

### **5️⃣ Run the Program**

```
python3 pan_tilt_expression_track.py
```

If the camera is working correctly:
• Face appears
• Servos rotate to center the face
• Smile detection prints in terminal

---

## **🧪 Testing With a Single Image (Optional)**

Capture:

```
rpicam-still -o test.jpg
```

Run detection:

```
python3 expression_detect_single.py
```

Output saved as `output.jpg`.

---

## **🚀 Conclusion**

This project demonstrates how Computer Vision and Robotics can be merged to build a **real-time intelligent camera system**.
You now have a working setup capable of face tracking, expression analysis, and pan–tilt motion control — all running directly on the Raspberry Pi.

---

## **📬 Contact**

**Developer:** Dhruv Devaliya
**LinkedIn:** [https://www.linkedin.com/in/dhruv-devaliya/](https://www.linkedin.com/in/dhruv-devaliya/)
**GitHub:** [https://github.com/Bit-Bard](https://github.com/Bit-Bard)
**Email:** *(dhruvdevaliya@gmail.com)*

---
