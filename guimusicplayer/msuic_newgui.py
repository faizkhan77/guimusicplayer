from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Music Player")
root.geometry("400x550")
root.configure(bg="#1e1e2f")  # Dark background for a modern look

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
    resume_btn.configure(text="⏸")
    resume_btn.configure(command=unpause)


def unpause():
    mixer.music.unpause()
    resume_btn.configure(text="⏵")
    resume_btn.configure(command=pausebtn)


def nextmusic():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs_list)  # Next song
    playmusic()


def prevmusic():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs_list)  # Previous song
    playmusic()


# Load songs when the app starts
load_songs()

# ---------------- UI Enhancements ----------------


# Header
headlab = Label(
    root,
    text="Faiz Music Player",
    font=("Verdana", 18, "bold"),
    bg="#1e1e2f",
    fg="white",
)
headlab.pack(pady=20)


# Music Frame
musicframe = Frame(root, bg="#2a2a3b", bd=10, relief="ridge")
lab = Label(
    musicframe, text="Playing Now", bg="#2a2a3b", fg="white", font=("Verdana", 12)
)
lab.pack(side=BOTTOM, pady=(0, 10))

# Album image
img = Image.open("musicimg.png")
resimg = img.resize((200, 200))
newimg = ImageTk.PhotoImage(resimg)

labimg = Label(musicframe, image=newimg, bg="#2a2a3b")
labimg.pack(anchor=CENTER, pady=30)

musicframe.pack(pady=(10, 35))
musicframe.pack_propagate(False)
musicframe.configure(height=300, width=350)


# Control Buttons Frame
buttonframe = Frame(root, bg="#1e1e2f")


# Previous Button
prev_btn = Button(
    buttonframe,
    text="⏮",  # Unicode character for previous
    bg="#ff5e5e",
    fg="white",
    font=("Verdana", 17),
    bd=0,
    relief=GROOVE,
    command=prevmusic,
    width=3,
)
prev_btn.grid(row=0, column=0, padx=20, pady=10)

# Play/Pause Button
resume_btn = Button(
    buttonframe,
    text="⏵",  # Unicode character for play
    bg="#1cd1a1",
    fg="white",
    font=("Verdana", 17),
    bd=0,
    relief=GROOVE,
    command=playmusic,
    width=3,
)
resume_btn.grid(row=0, column=1, padx=20, pady=10)

# Next Button
next_btn = Button(
    buttonframe,
    text="⏭",  # Unicode character for next
    bg="#ff5e5e",
    fg="white",
    font=("Verdana", 17),
    bd=0,
    relief=GROOVE,
    command=nextmusic,
    width=3,
)
next_btn.grid(row=0, column=2, padx=20, pady=10)

buttonframe.pack(pady=10)


# Mixer Initialization
mixer.init()
music_state = StringVar()
music_state.set("Choose one")

root.mainloop()
