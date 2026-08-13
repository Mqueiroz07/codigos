import pyautogui as py
import time

time.sleep(3)   
currentMouseX, currentMouseY = py.position()
print(f"Current mouse position: ({currentMouseX}, {currentMouseY})")