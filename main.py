import numpy as np
import cv2 as cv
import pyautogui
import mss
import win32gui, win32con
import vision, recording

print("Starting after 10 sec!")
pyautogui.sleep(10)

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = recording.get_monitor()

    while "Screen capturing":
        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        img = cv.cvtColor(img, cv.COLOR_RGBA2RGB)
        
        cv.imshow("Recording", vision.draw_circle(img))

        #always top most
        hWnd = win32gui.FindWindow(None, "Recording")
        win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Press "q" to quit
        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break
cv.waitKey()
