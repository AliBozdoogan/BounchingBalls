import tkinter as tkr
import time
import pyautogui
a=pyautogui.position() #get the mouse possition as x and y.
Ball_array = [] #to create balls array


def turn(a,b): #to again return value for loops
    if a % b == 0:
        a = 0
        return a
def turn1(a,b): #to again return value for loops
    if a % b == 0:
        a = 1
        return a
class Ball: #to create ball
    def __init__(self,x0,y0,x1,y1,z1,pos): #x0= xinitial coordinate y0=y initial coordinate x1 and y1 final coordinate
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.z1=z1
        canvas.create_oval(x0,y0,x1,y1,fill=z1) # we create ball from xo to x1 and y0 to y1, z1 is colour
        self.pos=canvas.coords=Ball_array #to get positions from balls

dx= [0,0,0,0,0]  #for x direction velocity
dy= [1,1,1,1,1]  #for y direction velocity
gravitiy=0.9     # for phsyics
friction=0.5     #for physics
root = tkr.Tk() #call library
root.title("Phase 1")
window_width,window_height = 300,400 #width and height of window

screen_width = root.winfo_screenwidth() #to get width our screen
screen_height = root.winfo_screenheight() #to get height our screen

position_top =int(screen_height/2-window_height/2) #1080/2 - 400/2 = 340
position_right =int(screen_width/2-window_width/2) #1920/2 - 300/2 = 810
print(" ",position_right,position_top) #to check values
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')  #to center window on our screen
canvas = tkr.Canvas(root, width=window_width,height=window_height) #create window
canvas.grid()
radius=60 #radius our balls
for a in range(0,300,radius): #to create 5 balls
        Ball_array.append((Ball(a,0,60+a,60,"light blue",Ball_array)))

id = canvas.create_line(0,60,300,60) #create line bottom of balls
while True:
    for x in range(1,5):
        for a in range (0,5): # check the all ball_arrays by using loops
            if Ball_array[a].pos[0]==Ball_array[x].pos[2] or  Ball_array[a].pos[2]==Ball_array[x].pos[0]: #check the left of the first ball and right of the second ball, varsa versa
                canvas.move(Ball_array[a],-dx[a],dy[a]) #if m is equal for balls, only change direction
                canvas.move(Ball_array[x],-dx[x],dy[x])
            if Ball_array[a].pos[1]==Ball_array[x].pos[3] or  Ball_array[a].pos[3]==Ball_array[x].pos[1]: #check top and bottom between balls and varsa versa
                canvas.move(Ball_array[a],dx[a],-dy[a]) #if m is equal for balls, only change direction
                canvas.move(Ball_array[x],dx[x],-dy[x])
            turn1(x,4) #for loops again return


    for x in range(0,5):
        for b in range(0,300,60): #to check mouse and balls positions and moving
            if position_right+b <= a[0] <= position_right+radius/2 and (position_top+370) <= a[1] <= (position_top+385):
                dx[x] += 2 # speed up to +x direction
            if position_right+radius/2+b<=a[0]<=position_right+radius and position_top+385 <= a[1] <=position_top+400:
                dx[x] -= 2 # speed up to -x direction
            if position_right+b<=a[0]<=position_right+radius and a[1] >=position_top+385:
                dy[x] -= 2 # speed up to -y direction
            turn(x,4) # return for loops again

        canvas.move(Ball_array[0],dx[0],dy[0]) #to move by using dx[0] and dy[0]
        pos = canvas.coords(Ball_array[0]) # to get position Ball_array[0]

        canvas.move(Ball_array[1], dx[1],dy[1]) #to move by using dx[1] and dy[1]
        pos1 = canvas.coords(Ball_array[1]) # to get position Ball_array[1]

        canvas.move(Ball_array[2], dx[2],dy[2]) #to move by using dx[2] and dy[2]
        pos2 = canvas.coords(Ball_array[2]) # to get position Ball_array[2]

        canvas.move(Ball_array[3], dx[3],dy[3]) #to move by using dx[3] and dy[3]
        pos3 = canvas.coords(Ball_array[3]) # to get position Ball_array[3]

        canvas.move(Ball_array[4], dx[4],dy[4]) #to move by using dx[4] and dy[4]
        pos4 = canvas.coords(Ball_array[5]) # to get position Ball_array[4]

        for x in range(0,5):
                    if Ball_array[x].pos[3] >= 400 and dy[x] <= 2: # check the borders and return zeros
                        dx[x]=0
                        dy[x]=0
                        gravitiy=0
                        friction=0

                    if Ball_array[x].pos[3] >= 400 or Ball_array[x].pos[1] <=1: # check the bottom and top, change direction
                        dy[x] *= -1

                    if Ball_array[x].pos[2] >= 300 or Ball_array[x].pos[0] <=1: # check the right and left, change direction
                        dx[x] = -(dx[x]*friction)

                    root.update() # update window

                    dy[x] += gravitiy # always apply gravity for y direction for physics
                    turn(x,4) #return again for loops
                    time.sleep(0.025) # for moving speed

root.mainloop()