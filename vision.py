import pyautogui
import cv2 as cv
import numpy as np

"""Computing Vision"""
#red mask (RGB)
#low_red = np.flip(np.array([190, 30, 30])) for only day
low_red = np.flip(np.array([90, 19, 29])) #day + night mode
high_red = np.flip(np.array([230, 50, 50]))
boxWeight, boxHeight = (64,64)

#finding a rod float on part of screen
def find_float(image):
    global low_red, high_red
    mask = cv.inRange(image, low_red, high_red)  
    #get all non zero values
    coord=cv.findNonZero(mask)

    if(coord != "None"):
        return coord
    else: 
        return False    


def draw_circle(image):
    global boxWeight,boxHeight
    try: 
        (x_float,y_float) = find_float(image)[0][0]
        color = (0, 255, 255)
        thickness = 2
        image = cv.rectangle(image, (x_float-boxWeight//2, y_float-boxHeight//2), (x_float + 64, y_float + 64), (0,255,255), 1)
        image = cv.putText(image,"Rod float",(x_float - boxWeight//2, y_float - boxHeight),cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
        return image 
    except:
        #print("Not Found")
        pyautogui.rightClick()
        pyautogui.sleep(1)
        return image