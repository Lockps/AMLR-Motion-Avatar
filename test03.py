import subprocess
import sys
import os
import keyboard
import time

subprocess.run('start microsoft.windows.camera:',shell=True)
print("camera opened successful")
print("wait for 1 sec")
time.sleep(1)
keyboard.press_and_release('space')
print("img Captured") 
print("wait for 0.5 sec for turn on video capture")
time.sleep(0.5)

keyboard.press_and_release('space')
time.sleep(10)
keyboard.press_and_release("space")
print("video stopped")
subprocess.run('Taskkill /IM WindowsCamera.exe /F' , shell=True)
print("close!")