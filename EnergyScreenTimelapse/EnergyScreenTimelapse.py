import cv2
import numpy as np
import pyautogui
from time import sleep
from tkinter import *

win = Tk()
win.geometry("270x150")
win.title('Energy screen timelapse')
win.iconbitmap('icon.ico')

screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter('output/output.mp4',fourcc,20.0,(screen_size))

br = False

def quit():
	br = True

def start():
	frameskip = var.get()
	getSpeed = var.get()
	lapseName = e1.get()
	out = cv2.VideoWriter('output/'+str(lapseName)+'.mp4',fourcc,20.0,(screen_size))
	try:
		while True:
			if frameskip == getSpeed:
				img = pyautogui.screenshot()
				frame = np.array(img)
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				out.write(frame)
				frameskip = 0
			#cv2.imshow("show",frame)
			if br == True:
				break
			frameskip += 1
			win.update()
	except:
		exit()

var = DoubleVar()

B1 = Button(win, text='Start', width = '5', command=start).grid(column='1',row='1',pady='10',padx='10')
B2 = Button(win, text='Quit', width = '5', command=quit).grid(column='0',row='1',pady='10',padx='10')
L1 = Label(win, text='speed of timelapse').grid(column='2',row='0')
s = Scale(win, from_=1, to=100, orient=HORIZONTAL, variable = var).grid(column='2',row='1',pady='10',padx='10')
l2 = Label(win, text='name your timelapse').grid(column='1', row='2')
e1 = Entry(win, width=15)
e1.grid(column='1', row='3')

win.mainloop()