import tkinter as tkr
import time
import mouse
from pynput.mouse import Listener
from array import *

class Ball:
    def __init__(self,x0,y0,x1,y1,z1):
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.z1=z1
        canvas.create_oval(x0,y0,x1,y1,fill=z1)

dx= [3,1,0,0,0]
dy= [3,1,1,1,1]
gravitiy=0.9
friction=0.5

tk1 = tkr.Tk()
canvas = tkr.Canvas(tk1, width=300,height=400)
canvas.grid()
ball= canvas.create_oval(0,0,60,60,fill="light blue")
ball1= canvas.create_oval(60,0,120,60,fill="light blue")
ball2= canvas.create_oval(120,0,180,60,fill="light blue")
ball3= canvas.create_oval(180,0,240,60,fill="light blue")
ball4= canvas.create_oval(240,0,300,60,fill="light blue")
id = canvas.create_line(0,60,300,60)
tk1.title("Use this one")

while True:
    canvas.move(ball,dx[0],dy[0])
    pos = canvas.coords(ball)

    canvas.move(ball1, dx[1],dy[1])
    pos1 = canvas.coords(ball1)

    canvas.move(ball2, dx[2],dy[2])
    pos2 = canvas.coords(ball2)

    canvas.move(ball3, dx[3],dy[3])
    pos3 = canvas.coords(ball3)

    canvas.move(ball4, dx[4],dy[4])
    pos4 = canvas.coords(ball4)

    for x in range(0,5):
                if pos[3] >= 400 and dy[x] <= 2:
                    dx[x]=0
                    dy[x]=0
                    gravitiy=0
                    friction=0
                if pos[0] == pos1[2] or pos[2] == pos2[0]:
                    dx[0] *= -1
                    dy[0] *= -1
                    dx[1] *= -1
                    dy[1] *= -1

                    canvas.move(ball, dx[0], dy[0])
                    canvas.move(ball1, dx[1], dy[1])

                if pos[3] >= 400 or pos[1] <=1:
                    dy[x] *= -1

                if pos[2] >= 300 or pos[0] <=1:
                    dx[x] = -(dx[x]*friction)

                tk1.update()

                dy[x] += gravitiy

                #print(on_click())
                time.sleep(0.025)


tk1.mainloop()