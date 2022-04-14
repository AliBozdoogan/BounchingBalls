# from pynput.mouse import Button, Controller
# def on_mouse_press(self,x,y,button,modifiers):
#     self.center_x =x
#     self.center_y =y
#
# mouse = Controller()
# # print(mouse.position[0])
#
# if mouse.left_click() == True :
#     print(mouse.position[0])

import mouse

from pynput.mouse import Listener
from array import *

def on_click(x, y, button, pressed):
    global array
    if pressed:

        array =format(x)

        #print(array)



        print(("Mouse clicked at ({0}, {1}) with {2}").format(x,y,button))

with Listener(on_click=on_click) as listener:
    listener.join()
print("asdasd")
a=on_click()
print(a)

