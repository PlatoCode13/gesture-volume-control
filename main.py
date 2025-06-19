import cv2
import time
import pyautogui
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

# Volume setup using pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

# Webcam setup
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)
pTime = 0
lastGesture = None  # To avoid repeated execution

print("✅ Gesture Control Active — Use gestures in front of the camera.")

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = detector.fingersUp()

        # === Detect gestures ===

        # 1. Play/Pause — All fingers up
        if fingers == [1, 1, 1, 1, 1] and lastGesture != "playpause":
            pyautogui.press('k')
            print("▶️ Play/Pause triggered")
            lastGesture = "playpause"
            time.sleep(1)

        # 2. Next track — Thumb only
        elif fingers == [1, 0, 0, 0, 0] and lastGesture != "next":
            pyautogui.press('l')
            print("⏭️ Next Track triggered")
            lastGesture = "next"
            time.sleep(1)

        # 3. Fist — Exit
        elif fingers == [0, 0, 0, 0, 0] and lastGesture != "exit":
            print("👋 Exit Gesture Detected")
            break

        # 4. Volume Up — Thumb + Index close
        elif lastGesture != "volume_up":
            length, _, _ = detector.findDistance(4, 8, img, draw=False)
            if length < 40:
                vol = volume.GetMasterVolumeLevelScalar()
                newVol = min(vol + 0.05, 1.0)
                volume.SetMasterVolumeLevelScalar(newVol, None)
                print("🔊 Volume Up")
                lastGesture = "volume_up"
                time.sleep(0.5)

        # 5. Volume Down — Thumb + Middle close
        elif lastGesture != "volume_down":
            length, _, _ = detector.findDistance(4, 12, img, draw=False)
            if length < 40:
                vol = volume.GetMasterVolumeLevelScalar()
                newVol = max(vol - 0.05, 0.0)
                volume.SetMasterVolumeLevelScalar(newVol, None)
                print("🔉 Volume Down")
                lastGesture = "volume_down"
                time.sleep(0.5)

        # Reset if hand moved away
        else:
            lastGesture = None

    # FPS display
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cv2.imshow("Gesture Control", img)
    if cv2.waitKey(1) == ord('q'):
        print("🛑 Exiting via 'q'")
        break

cap.release()
cv2.destroyAllWindows()
