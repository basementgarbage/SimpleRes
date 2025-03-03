import pystray
import PIL.Image
import win32api
import win32con


def ChangeRes(width, height):
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    devmode.PelsWidth = width
    devmode.PelsHeight = height
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
    result = win32api.ChangeDisplaySettings(devmode, 0)
 
image = PIL.Image.open("logo.png")

def MenuLogic(icon, item):
    if str(item) == "1920x1080":
        ChangeRes(1920, 1080)
    elif str(item) == "1280x960":
        ChangeRes(1280, 960)
    elif str(item) == "1280x1024":
        ChangeRes(1280, 1024)
    elif str(item) == "1440x1024":
        ChangeRes(1440, 1080)
    elif str(item) == "1440x900":
        ChangeRes(1440, 900)
    elif str(item) == "Exit":
        icon.stop()



icon = pystray.Icon("SimpleRes", image, menu=pystray.Menu(
    
     pystray.MenuItem("1920x1080", MenuLogic),
     pystray.MenuItem("1280x960", MenuLogic),
     pystray.MenuItem("1280x1024", MenuLogic),
     pystray.MenuItem("1440x1024", MenuLogic),
     pystray.MenuItem("1440x900", MenuLogic),
     pystray.MenuItem("Exit", MenuLogic),
))


icon.run()