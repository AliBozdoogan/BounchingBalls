import tkinter as tkr
import time


dx= [0,0,0,0,0]
dy= [1,1,1,1,1]
gravitiy=0.9
friction=0.5
root = tkr.Tk()
root.title("Phase 1")

window_width,window_height = 300,400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top =int(screen_height/2-window_height/2)
position_right =int(screen_width/2-window_width/2)
print(" ",position_right,position_top)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
canvas = tkr.Canvas(root, width=window_width,height=window_height)
canvas.grid()

ball= canvas.create_oval(0,0,60,60,fill="light blue")
ball1= canvas.create_oval(60,0,120,60,fill="light blue")
ball2= canvas.create_oval(120,0,180,60,fill="light blue")
ball3= canvas.create_oval(180,0,240,60,fill="light blue")
ball4= canvas.create_oval(240,0,300,60,fill="light blue")
id = canvas.create_line(0,60,300,60)

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

                if pos[3] >= 400 or pos[1] <=1:
                    dy[x] *= -1

                if pos[2] >= 300 or pos[0] <=1:
                    dx[x] = -(dx[x]*friction)

                root.update()

                dy[x] += gravitiy

                time.sleep(0.025)

root.mainloop()