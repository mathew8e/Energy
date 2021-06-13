import cv2
import numpy as np
import pyautogui
from time import sleep
import eel
import io
import sys


def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        exit()


eel.init('web')

screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter('output/output.mp4',fourcc,20.0,(screen_size))

@eel.expose
def start(frameskip, getSpeed, lapsName):
	out = cv2.VideoWriter('output/'+str(lapsName)+'.mp4',fourcc,20.0,(screen_size))
	try:
		while True:
			if frameskip == getSpeed:
				img = pyautogui.screenshot()
				frame = np.array(img)
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				out.write(frame)
				frameskip = 0
			#cv2.imshow("show",frame)
			frameskip += 1
			print("Frame taken...")
	except:
		print(sys.exc_info()[0])
		exit()

@eel.expose
def stop():
	print("stopping..")
	quit()

eel.start('index.html', size=(700, 600), close_callback=close_callback)

