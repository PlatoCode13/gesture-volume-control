# 🔊 Gesture Volume Control (Python + OpenCV + MediaPipe + Pycaw)

Control your system volume using **hand gestures** via your webcam.  
This Python project detects your hand, tracks your index and thumb finger distance, and adjusts the volume accordingly.

---

## 📸 Features

- 📷 Real-time hand detection with MediaPipe
- 🖐️ Volume control using index and thumb pinch
- ✅ Smooth UI with visual volume bar
- 🧠 Only sets volume if pinky is folded (a safety gesture)
- ⚡ Displays current volume and FPS

---

## 🖥️ Requirements

- Windows OS (10 or later)
- Python 3.10+
- A working webcam

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/your-username/gesture-volume-control.git
cd gesture-volume-control
```
2. Create a Virtual Environment
```
python -m venv .venv
.venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Script
```
python main.py
```
📐 How It Works
MediaPipe Hands detects 21 hand landmarks.

The distance between thumb and index is mapped to a system volume range.

If pinky is down, the volume is applied.

Displays:

🔊 Volume % bar

📈 FPS for performance

🟩 Green confirmation circle when volume is set

🧩 Dependencies
Listed in requirements.txt:

opencv-python

mediapipe

numpy

pycaw

comtypes

👋 Example Gestures
Gesture	Action
Thumb + Index pinch (close)	Volume Down
Thumb + Index pinch (wide)	Volume Up
Pinky up	Disable volume control (preview only)
Pinky down	Confirm volume change

📄 License
MIT License – free to use, share, and modify.

🙌 Acknowledgments
MediaPipe by Google

Pycaw by André Miras
