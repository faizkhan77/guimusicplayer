from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Music Player")
root.geometry('400x550')
root.configure(bg="cyan")

headlab = Label(root, text="Faiz Music Player", font=("bold", 10, "italic"), bg="cyan")
headlab.pack()

# All Functions

def playmusic():

    def pausebtn():
        
        def unpause():
            lab['text'] = running
            mixer.music.unpause()
            resume_btn.configure(text=" || ")
            resume_btn.configure(command=pausebtn)

        mixer.music.pause()
        lab.configure(text="Song is Paused")
        resume_btn.configure(text=" ▶ ")
        resume_btn.configure(command=unpause)

    running = listb.get(ACTIVE)

    lab['text'] = running
    # mixer.init()
    mixer.music.load(running)
    mixer.music.play()

    resume_btn.configure(text=" || ")
    resume_btn.configure(command=pausebtn)

def startmusic():
    running = listb.get(ACTIVE)

    lab['text'] = running
    # mixer.init()
    mixer.music.load(running)
    mixer.music.play()

def musicrewind():
    mixer.music.rewind()


def stopmusic():
    mixer.music.stop()
    # root.destroy()


def playlist_btn():
    global listb
    global songs
    global show
    playlist_win = Toplevel(root)
    playlist_win.configure(bg="cyan")
    playlist_win.geometry('350x400')
    playlist_win.title("Songs Playlists")

    labe1 = Label(playlist_win, text="Faiz Music Playlist", font=("bold", 15, "italic"), bg="cyan")
    labe1.pack(pady=(5, 0))

    playlist_frame = Frame(playlist_win, height=150, width=300, bg="red")


    listb = Listbox(playlist_frame, selectmode=SINGLE, width=35, height=20, font=("ariel 9 bold", 10), bg="red", fg="cyan")
    listb.grid(row=0, column=0)

    scrollb = Scrollbar(playlist_frame, width=20)
    scrollb.grid(row=0, column=1, sticky=N+S)

    listb.config(yscrollcommand=scrollb.set)
    scrollb.config(command= listb.yview)

    playlist_frame.pack(pady=(10, 5))

    os.chdir(r"C:\Users\hp\Music")
    songs = os.listdir()

    def show():      
        for i in songs:
            listb.insert(END, i)
    show()

def nextmusic():
    playing = lab['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listb.delete(0, END)
    show()
    listb.select_set(new_index)
    lab['text'] = playing

def prevmusic():
    playing = lab['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listb.delete(0, END)
    show()
    listb.select_set(new_index)
    lab['text'] = playing

# Music Frame

musicframe = Frame(root, bg="red")

lab = Label(musicframe, text="PLay a Music", bg="red", font=("bold", 15))
lab.pack(side=BOTTOM, pady=(0, 10))

img = Image.open('musicimg.png')
resimg = img.resize((200, 200))
newimg = ImageTk.PhotoImage(resimg)

labimg = Label(musicframe, image=newimg, bg="red")
labimg.pack(anchor=CENTER, pady=30)

musicframe.pack(pady=(10,35))
musicframe.pack_propagate(False)
musicframe.configure(height=300, width=350)



buttonframe = Frame(root, bg="cyan")

rewindbtn_frame = Frame(buttonframe, highlightbackground='green', highlightthickness=1)
rewind_btn = Button(rewindbtn_frame, text=" ⋘ ", bg="cyan", fg="green", font=("bold", 17), bd=0,
                    command = musicrewind)
rewind_btn.pack()
rewindbtn_frame.place(x=15, y=5)


prevbtn_frame = Frame(buttonframe, highlightbackground='blue', highlightthickness=1)
prev_btn = Button(prevbtn_frame, text=" « ", bg="cyan", fg="blue", font=("bold", 17), bd=0,
                    command=prevmusic)
prev_btn.pack()
prevbtn_frame.place(x=82, y=5)


resumebtn_frame = Frame(buttonframe, highlightbackground='red', highlightthickness=1)
resume_btn = Button(resumebtn_frame, text=" ▶ ", bg="cyan", fg="red", font=("bold", 17), bd=0,
                    command=playmusic)
resume_btn.pack()
resumebtn_frame.pack(pady=(5, 0))


nextbtn_frame = Frame(buttonframe, highlightbackground='blue', highlightthickness=1)
next_btn = Button(nextbtn_frame, text=" » ", bg="cyan", fg="blue", font=("bold", 17), bd=0,
                    command=nextmusic)
next_btn.pack()
nextbtn_frame.place(x=227, y=5)


stopbtn_frame = Frame(buttonframe, highlightbackground='green', highlightthickness=1)
stop_btn = Button(stopbtn_frame, text="㊀", bg="cyan", fg="green", font=("bold", 17), bd=0,
                    command = stopmusic)
stop_btn.pack()
stopbtn_frame.place(x=294, y=5)



startbtn_frame = Frame(buttonframe, highlightbackground='red', highlightthickness=1)
start_btn = Button(startbtn_frame, text=" s ", bg="cyan", fg="red", font=("bold", 17), bd=0,
                    command=startmusic)
start_btn.pack()
startbtn_frame.place(x=115, y=58)


exitbtn_frame = Frame(buttonframe, highlightbackground='red', highlightthickness=1)
exit_btn = Button(exitbtn_frame, text=" x ", bg="cyan", fg="red", font=("bold", 17), bd=0,
                    command= root.destroy)
exit_btn.pack()
exitbtn_frame.place(x=190, y=58)



playlistbtn = Button(buttonframe, text="Playlist", font=("bold", 20, "italic"), bg="cyan", command=playlist_btn)
playlistbtn.pack(side=BOTTOM, fill=X)

buttonframe.pack()
buttonframe.pack_propagate(False)
buttonframe.configure(height=160, width=350)


mixer.init()
music_state = StringVar()
music_state.set("Choose one")

root.mainloop()