import pystray
from pystray import MenuItem as item
from PIL import Image
import time

def on_clicked(icon, item):
    if str(item) == 'Quit':
        icon.stop()
    elif str(item) == 'Notify':
        icon.notify("My App", "This is a notification!") # Убрали icon=pystray.icons.information

image = Image.open("icon.png") # Убедитесь, что icon.png существует

menu = (item('Notify', on_clicked), item('Quit', on_clicked))
icon = pystray.Icon("My App", image, menu=menu)
icon.run()

