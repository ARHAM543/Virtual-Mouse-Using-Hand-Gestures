import cv2
import numpy as np
import time
import pyautogui
import HandTrackingModule as htm

def run_script():
    print("VirtualMouse script executed!")
    return "VirtualMouse script executed successfully!"

if __name__ == "__main__":
    print(run_script())

# Camera settings
wCam, hCam = 760, 600
frameR = 100  # Reduce edge area where hand movements will be considered
smoothening = 5  # Smoothing factor for better movement control

# Initialize variables
pTime = 0
plocX, plocY = 0, 0  # Previous location of the cursor
clocX, clocY = 0, 0  # Current location of the cursor
lastRightClickTime = 0  # Track time for cooldown between right-clicks
lastLeftClickTime = 0  # Track time for cooldown between left clicks
rightClickCooldown = 2  # Cooldown duration for right-click in seconds
leftClickCooldown = 3  # Cooldown duration for left-click in seconds

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Using DSHOW for better webcam performance on Windows
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(maxHands=1)  # Detecting only one hand for simplicity

# Get screen size
wScr, hScr = pyautogui.size()

while True:
    success, img = cap.read()

    # Find hand landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:  # Check if landmarks are detected
        # Index finger tip position
        x1, y1 = lmList[8][1:]

        # Get the positions as relative to the screen size (mapping screen coordinates)
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

        # Smooth the movement
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # Move the mouse
        pyautogui.moveTo(wScr - clocX, clocY)

        plocX, plocY = clocX, clocY

        # Optional: Drawing a circle to indicate finger position
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

        # Detect gestures
        fingers = detector.fingersUp()

        # Get current time
        currentTime = time.time()

        # Right-click gesture (pinky alone or pinky + index)
        if fingers[4] == 1 and (fingers[1] == 0 or fingers[1] == 1): 
             # Pinky raised, index may or may not be raised
            if currentTime - lastRightClickTime > rightClickCooldown:  # Check cooldown
                pyautogui.rightClick()
                lastRightClickTime = currentTime

        # Left-click gesture (index and middle fingers up)
        if fingers[1] == 1 and fingers[2] == 1: 
            length, img, lineInfo = detector.findDistance(8, 12, img) # Index and middle fingers are raised
            if currentTime - lastLeftClickTime > leftClickCooldown:  # Check cooldown
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()  # Perform a left click
                lastLeftClickTime = currentTime
        
        # Left-click gesture (index, middle, and ring fingers up) without cooldown
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:  # Index, middle, and ring fingers are raised
            pyautogui.click()  # Perform a left click without cooldown

    # Frame rate calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    # Display the frame
    cv2.imshow("Virtual Mouse", img)
    cv2.waitKey(1)
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()