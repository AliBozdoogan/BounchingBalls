from tkinter import *

root = Tk()
root.title("Phase 1")

window_width,window_height = 300,400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top =int(screen_height/2-window_height/2)
position_right =int(screen_width/2-window_width/2)
print(position_right,position_top)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

root.mainloop()
