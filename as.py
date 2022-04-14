import tkinter as tkr
import time
Ball_array = []
# global x0,y0,x1,y1,z1
class Ball:
    def __init__(self,x0,y0,x1,y1,z1):
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.z1=z1
        canvas.create_oval(x0,y0,x1,y1,fill=z1)




    def pos(self,Ball_array[]):
        # self.canvas=canvas
        # self.x0 = x0
        # self.y0 = y0
        # self.x1 = x1
        # self.y1 = y1
        # self.z1 = z1
        # ball=Ball(x0,y0,x1,y1,z1)
        pos1 = canvas.coords(Ball)
        Left = pos1[0]
        Top = pos1[1]
        Right = pos1[2]
        Bottom = pos1[3]
        Possition = [Left, Top, Right, Bottom]

        return Possition
dx=0
dy=0
gravitiy=0.7
friction=0.5

tk = tkr.Tk()
canvas = tkr.Canvas(tk, width=300,height=500)
canvas.grid()
# Ball1=Ball(0,0,60,60,"light blue")
# Ball2=Ball(60,0,120,60,"light blue")
# Ball3=Ball(120,0,180,60,"light blue")
# Ball4=Ball(180,0,240,60,"light blue")
# Ball5=Ball(240,0,300,60,"light blue")
# pos1=Ball.pos()

# Ball_array.append((Ball(0,0,60,60,"light blue")))
# Ball_array.append((Ball(60,0,120,60,"light blue")))
# Ball_array.append((Ball(120,0,180,60,"light blue")))
# Ball_array.append((Ball(180,0,240,60,"light blue")))
# Ball_array.append((Ball(240,0,300,60,"light blue")))
#for x in range(0,5):
for a in range(0,300,60):
        Ball_array.append((Ball(a,0,60+a,60,"light blue")))
# Position = Ball_array[0]


# print(Ball_array[0])

while True:
    canvas.move(Ball_array[0],dx,dy)
    pos

    canvas.move(Ball_array[1], dx, dy)
    # pos1 = canvas.coords(Ball2)

    canvas.move(Ball_array[2], dx, dy)
    # pos2 = canvas.coords(Ball3)

    canvas.move(Ball_array[3], dx, dy)
    # pos3 = canvas.coords(Ball4)

    canvas.move(Ball_array[4], dx, dy)
    # pos4 = canvas.coords(Ball5)

    if Position[0] >= 400 and dy <= 2:
        dx=0
        dy=0
        gravitiy=0
        friction=0

    if Ball1[3] >= 400 :
        dy *= -1

    if Ball1.pos[1] <= 1:
        dy *= -1

    if Ball1.pos[2] >= 300 :
        dx = -(dx*friction)

    if Ball1.pos[0] <= 1:
        dx = -(dx * friction)


    tk.update()

    dy += gravitiy

    time.sleep(0.025)


tk.mainloop()