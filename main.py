import time

import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome To Midhun's Kingdom")
print("Speaking Robo 2.0 Version is Created...")
text = input("Enter what you want to hear from Robo")
speak.Speak(text)
time.sleep(3)
text='Do you want me to speak more??'
speak.Speak(text)
text = input("Enter what you want to hear from Robo")
speak.Speak(text)

# # this code only work in windows machine
# time.sleep(3) is used to give a gap/pause in speaking,where 3s is the time gap
