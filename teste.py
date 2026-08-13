from numpy import number


f: any
a: any
b: any
if  'f' == ('a ' + 'b')**2 :
    'f'== a**2 + 2*a*b + b**2
#-------------------
#IMPORTANTE
import pyautogui as py
import time

currentMouseX, currentMouseY = py.position()
print(f"Current mouse position: ({currentMouseX}, {currentMouseY})")