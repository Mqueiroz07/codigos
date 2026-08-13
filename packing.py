import pyautogui as py
import time

py.FAILSAFE = True

py.click(36, 521)
time.sleep(3)
py.click(521, 343)
time.sleep(3)

while True:
    try:
        time.sleep(3)
        py.click(199, 474)
        time.sleep(3)
        py.click(898, 217)
        time.sleep(3)
        py.click(676, 430)
        time.sleep(3)
        py.press(keys='y')
        time.sleep(3)
    except py.FailSafeException:
        print("Programa interrompido pelo usuário.")
        break