import cv2
import numpy as np
import pyautogui
from time import sleep
import eel
import io
import sys
import asyncio

exitcode = 0

def close_callback(route, websockets):
	global exitcode, loop
	exitcode = True
	if not websockets:
		print('Bye!')
		loop.stop()
		sys.exit()
		exit()


eel.init('web')

screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter('output/output.mp4',fourcc,20.0,(screen_size))

@eel.expose
def start(lapsName):
	global out
	print(lapsName)
	out = cv2.VideoWriter('output/'+str(lapsName)+'.mp4',fourcc,20.0,(screen_size))


@eel.expose
def frameLoop(s):
	global out, loop
	img = pyautogui.screenshot()
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	frameskip = 0
	cv2.imshow("show",frame)
	print("Frame taken...")
	sleep(int(s))

def asyncfunc(s):
	global loop
	print("start")
	loop = asyncio.get_event_loop(s)	
	loop.run_forever()

@eel.expose
def stop():
	global exitcode
	sleep(1)
	print("stopping..")
	sys.exit()
	exit()
@eel.expose
def write(a):
	sleep(0.1)
	print(a)


eel.start('index.html', size=(700, 600), close_callback=close_callback)

