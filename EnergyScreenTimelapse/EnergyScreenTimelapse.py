import cv2
import numpy as np
import pyautogui
from time import sleep
import async_eel
import io
import sys
import asyncio

loop = asyncio.get_event_loop()

def close_callback(route, websockets):
	exitcode = True
	if not websockets:
		print('Bye!')
		loop.close()
		sys.exit()
		exit()



screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
	


@async_eel.expose
async def frameLoop(speed, lapsName):
	global fourcc, screen_size
	out = cv2.VideoWriter('output/test.mp4',fourcc,20.0,(screen_size))
	while loop.is_running():
		img = pyautogui.screenshot()
		frame = np.array(img)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		out.write(frame)
		#cv2.imshow("show",frame)
		print("Frame taken...")
		await asyncio.sleep(int(speed))


@async_eel.expose
async def stop():
	sleep(1)
	print("stopping..")
	loop.close()
	sys.exit()
	await exit()

@async_eel.expose
def write(a):
	sleep(0.1)
	print(a)

async def main():
	async_eel.init('web')
	await async_eel.start('index.html', size=(700, 600), close_callback=close_callback)

if __name__ == "__main__":
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()

