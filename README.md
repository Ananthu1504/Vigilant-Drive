# 🚗 Vigilant Drive - Driver Drowsiness Detection System

**Vigilant Drive** is a real-time driver alertness monitoring system built using **OpenCV**, **Dlib**, and **Raspberry Pi 4** with a **night vision camera**. The system detects whether the driver is active, drowsy, or sleeping by analyzing the eye aspect ratio using facial landmarks.

When the driver is detected as sleeping, an alert sound is played through a connected speaker using `pygame`.

---

## 📷 How It Works

- A night vision camera captures live video of the driver's face.
- Dlib’s `shape_predictor_68_face_landmarks` model is used to identify facial landmarks.
- Eye aspect ratio (EAR) is calculated to determine eye closure.
- Based on EAR:
  - **Active**: Eyes open
  - **Drowsy**: Eyes starting to close
  - **Sleeping**: Eyes closed — alarm is triggered
- Alert sound is played using a `.wav` file when sleep is detected.

---

## 🧰 Technologies Used

- **Python 3**
- **OpenCV**
- **Dlib**
- **imutils**
- **pygame**
- **NumPy**
- **Raspberry Pi 4**
- **Night Vision Camera Module**

---

## 📁 Project Structure
```
vigilant-drive/
├── vigilant_drive.py # Main Python script
├── wakeup.wav # Alarm audio file
├── driver_active.jpg # Sample image: active state
├── driver_sleeping.jpg # Sample image: sleeping state
├── Vigilant_Drive_Report.pdf # Project report (PDF)
├── README.md # This file
└── .gitignore
```


---

## 📥 Required Model File

This project uses Dlib’s **68 facial landmarks model**, which must be downloaded separately due to its large size.

👉 **[Download shape_predictor_68_face_landmarks.dat.bz2](https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2)**

> After downloading:
> 1. Extract the `.bz2` file using any archive tool (e.g., 7-Zip or WinRAR)
> 2. Place the extracted `shape_predictor_68_face_landmarks.dat` in the same folder as `vigilant_drive.py`

---

## 🔊 Audio Alert

The audio alert is a preloaded `.wav` file named `wakeup.wav` — a loud "Wake Up!" sound (from the Minions 🎙️) used to jolt the driver back to alertness.

---

## 🖼️ Screenshots

| Homepage | Detection | Alert |
|---------|-----------|--------|
| ![Active](images/driver_active.jpg) | ![Sleeping](images/driver_sleeping.jpg) |

---

## 📚 Report

You can find the detailed explanation of the system, hardware design, and software logic in the included report:  
📄 `Vigilant_Drive_Report.pdf`

---

## 👨‍🔬 Authors & Credits

- Developed by **Ananthu Krishna** as a college project.
- Uses open-source libraries: [Dlib](http://dlib.net/), [OpenCV](https://opencv.org/)

---

## 📜 License

This project is for academic and educational purposes only.

