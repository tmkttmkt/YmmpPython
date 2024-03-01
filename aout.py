import pyautogui
import time
import cv2
import numpy
img = cv2.imread("map.png")

p=pyautogui.locateOnScreen('ten.png' , confidence=0.8)
print(p)
if p!=None:
    cv2.rectangle(img, (p.left,p.top),(p.left+p.width,p.top+p.height),(255, 0, 0))
    p2=pyautogui.locateOnScreen('syouten.png' , confidence=0.8)
    print(p2)
    if p2!=None:
        
        cv2.rectangle(img, (p2.left,p2.top),(p2.left+p2.width,p2.top+p2.height),(255, 0, 0))

        cv2.imwrite('exp_rss.png', img)