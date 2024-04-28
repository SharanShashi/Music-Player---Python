from  tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer



#colors
co1 = "#ffffff" #white
co2 = "#3C1DC6" #purple
co3 = "#333333" #black
co4 = "#CFC7F8" #light purple

Window = Tk()
Window.title("")
Window.geometry('352x255')
Window.configure(background=co1)
Window.resizable(width=False, height= False)


#Events
def play_music():
    running = Listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    Listbox.delete(0, END)

    show()

    Listbox.select_set(new_index)
    running_song['text'] = playing

def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    Listbox.delete(0, END)

    show()

    Listbox.select_set(new_index)
    running_song['text'] = playing


#frames
left_frame = Frame(Window, width=150, height= 150, bg =co1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(Window, width=250, height= 150, bg =co3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(Window, width=400, height= 100, bg =co4)
down_frame.grid(row=1, column=0,columnspan=3, padx=0, pady=1)

#right frame
Listbox = Listbox(right_frame,selectmode=SINGLE, font=("Arial 9 bold"),width=22, bg=co3,fg=co1)
Listbox.grid(row=0, column=0)



w = Scrollbar(right_frame)
w.grid(row=0, column=1)

Listbox.config(yscrollcommand=w.set)
w.config(command=Listbox.yview)


#images
img_1 = Image.open("icons/3.jpg")
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=130, image= img_1, padx= 10,bg= co1)
app_image.place(x=10, y=15)

img_2 = Image.open("icons/3.jpg")
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=40, height=40, image=img_2, padx= 10,bg= co1, font=("Ivy 10"),command=play_music)
play_button.place(x=56+28, y=35)

img_3 = Image.open("icons/1.jpg")
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, width=40, height=40, image=img_3, padx= 10,bg= co1, font=("Ivy 10"),command=previous_music)
prev_button.place(x=10+28, y=35)

img_4 = Image.open("icons/2.jpg")
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width=40, height=40, image=img_4, padx= 10,bg= co1, font=("Ivy 10"),command=next_music)
next_button.place(x=102+28, y=35)

img_5 = Image.open("icons/4.jpg")
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width=40, height=40, image=img_5, padx= 10,bg= co1, font=("Ivy 10"),command=pause_music)
pause_button.place(x=148+28, y=35)

img_6 = Image.open("icons/3.jpg")
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, width=40, height=40, image=img_6, padx= 10,bg= co1, font=("Ivy 10"),command=continue_music)
continue_button.place(x=194+28, y=35)

img_7 = Image.open("icons/5.jpg")
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, width=40, height=40, image=img_7, padx= 10,bg= co1, font=("Ivy 10"),command=stop_music)
stop_button.place(x=240+28, y=35)


line = Label(left_frame,width=200, height=1, padx= 10, bg= co3)
line.place(x=0, y=1)

line = Label(left_frame,width=200, height=1, padx= 10, bg= co1)
line.place(x=0, y=3)

running_song = Label(down_frame, text="Choose a song",font=("Ivy 10") ,width=44, height=1, padx= 10, bg= co1,fg = co3,anchor=NW)
running_song.place(x=0, y=1)



os.chdir(r'Music')
songs = os.listdir()


def show():
    for i in songs:
        Listbox.insert(END, i)


show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

Window.mainloop()
