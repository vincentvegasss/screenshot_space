from collections import deque
import keyboard
import uuid
import time
from PIL import Image
from mss import mss
true=1
path="C:\\Users\\subas\Desktop\\GitHubProjects-111121\\img" #change the path!
mon={"top":750, "left":750, "width":1000, "height":1000}
sct= mss() #mss: multiple screenshots module/
record_id=uuid.uuid4()

is_exit= False
def exit():
    global is_exit
    is_exit=True
keyboard.add_hotkey("esc", exit)

while true:
    if is_exit:break
    elif keyboard.is_pressed("space"):
        time.sleep(0.1)
        img= sct.grab(mon)
        im= Image.frombytes("RGB",img.size, img.rgb)
        im.save(f"{path}/image2{record_id}.png")
        print("basarili")
    else: continue
 