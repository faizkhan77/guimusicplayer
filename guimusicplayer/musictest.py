from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Music Player")
root.geometry("400x550")
root.configure(bg="cyan")

headlab = Label(root, text="Faiz Music Player", font=("bold", 10, "italic"), bg="cyan")
headlab.pack()

# All Functions

# All Functions
current_song_index = 0
songs_list = []
song_folder = "songs/"


def load_songs():
    global songs_list
    for file in os.listdir(song_folder):
        if file.endswith(".mp3"):
            songs_list.append(file)


def playmusic():
    global current_song_index
    song = os.path.join(song_folder, songs_list[current_song_index])
    mixer.music.load(song)
    mixer.music.play()
    resume_btn.configure(command=pausebtn)


def pausebtn():
    mixer.music.pause()
    resume_btn.configure(text=" | | ")
    resume_btn.configure(command=unpause)


def unpause():
    mixer.music.unpause()
    resume_btn.configure(text=" ▶ ")
    resume_btn.configure(command=pausebtn)


def nextmusic():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(
        songs_list
    )  # Go to next song in the list
    playmusic()


def prevmusic():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(
        songs_list
    )  # Go to previous song in the list
    playmusic()


# Load songs when the app starts
load_songs()

# ----------------


# Music Frame

musicframe = Frame(root, bg="red")

lab = Label(musicframe, text="PLay a Music", bg="red", font=("bold", 15))
lab.pack(side=BOTTOM, pady=(0, 10))

img = Image.open("musicimg.png")
resimg = img.resize((200, 200))
newimg = ImageTk.PhotoImage(resimg)

labimg = Label(musicframe, image=newimg, bg="red")
labimg.pack(anchor=CENTER, pady=30)

musicframe.pack(pady=(10, 35))
musicframe.pack_propagate(False)
musicframe.configure(height=300, width=350)


buttonframe = Frame(root, bg="cyan")


prevbtn_frame = Frame(buttonframe, highlightbackground="blue", highlightthickness=1)
prev_btn = Button(
    prevbtn_frame,
    text=" « ",
    bg="cyan",
    fg="blue",
    font=("bold", 17),
    bd=0,
    command=prevmusic,
)
prev_btn.pack()
prevbtn_frame.place(x=82, y=5)


resumebtn_frame = Frame(buttonframe, highlightbackground="red", highlightthickness=1)
resume_btn = Button(
    resumebtn_frame,
    text=" ▶ ",
    bg="cyan",
    fg="red",
    font=("bold", 17),
    bd=0,
    command=playmusic,
)
resume_btn.pack()
resumebtn_frame.pack(pady=(5, 0))


nextbtn_frame = Frame(buttonframe, highlightbackground="blue", highlightthickness=1)
next_btn = Button(
    nextbtn_frame,
    text=" » ",
    bg="cyan",
    fg="blue",
    font=("bold", 17),
    bd=0,
    command=nextmusic,
)
next_btn.pack()
nextbtn_frame.place(x=227, y=5)


buttonframe.pack()
buttonframe.pack_propagate(False)
buttonframe.configure(height=160, width=350)


mixer.init()
music_state = StringVar()
music_state.set("Choose one")

root.mainloop()
