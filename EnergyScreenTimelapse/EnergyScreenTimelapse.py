import cv2
import numpy as np
import pyautogui
from time import sleep
import async_eel
import io
import sys
import asyncio
import tkinter 
import tkinter.filedialog as filedialog

loop = asyncio.get_event_loop()
directory_path = ""

def close_callback(route, websockets):
	exitcode = True
	if not websockets:
		print('Bye!')
		loop.stop()
		sys.exit()
		exit()


screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
	

@async_eel.expose
async def frameLoop(speed, lapsName):
	global fourcc, screen_size, directory_path
	out = cv2.VideoWriter(str(directory_path),fourcc,20.0,(screen_size))
	print("created file at ", directory_path)
	while loop.is_running():
		img = pyautogui.screenshot()
		frame = np.array(img)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		out.write(frame)
		#cv2.imshow("show",frame)
		print("Frame taken...")
		await asyncio.sleep(float(speed))


@async_eel.expose
async def stop():
	sleep(1)
	print("stopping..")
	loop.close()
	sys.exit()
	await exit()

@async_eel.expose
def write(a):
	print(a)

@async_eel.expose
def selectFolder():
	global directory_path
	print("Here")
	root = tkinter.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	directory_path = filedialog.asksaveasfilename(
                defaultextension='.mp4', filetypes=[("mp4", '*.mp4')],
                title="Choose filename")
	async_eel.writePath(directory_path)

async def main():
	async_eel.init('web')
	await async_eel.start('index.html', size=(700, 600), close_callback=close_callback)

if __name__ == "__main__":
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()

