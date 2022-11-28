from tkinter import *
from PIL import Image

root = Tk()

info = Image.open('soundwave.gif')
frames = info.n_frames
print(frames)
root.mainloop()