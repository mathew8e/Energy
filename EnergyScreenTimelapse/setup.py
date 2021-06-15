from cx_Freeze import setup, Executable

base = None    

executables = [Executable("EnergyScreenTimelapse.py", base=base)]
buildOptions = dict(include_files = [('C:/Users/mathe/Documents/C/coding/energy screen timelapse/Energy/EnergyScreenTimelapse/web')])

packages = ["cv2", "numpy", "pyautogui", "async_eel", "io", "sys", "asyncio", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "EnergyScreenTimelapse",
    options = dict(build_exe = buildOptions),
    version = "1.1",
    description = 'This is a program that records your screen',
    executables = executables
)