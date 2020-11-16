import os
from tkinter import *
import tkinter.font as tkFont
import random

App = Tk(className="Search")
App.iconbitmap('searchIcon.ico')
App.geometry("570x320")
App.configure(bg='#241e79')

fontStyle = tkFont.Font(family='Courier', size=13, weight='bold')

label = Label(text='Enter any text you think is included in the song name', width=100, height=2, fg='black', bg='#673ab7', font=fontStyle)
label.pack()

# an input field
input_field = Entry(App, bd=5, width=40, fg='dodgerblue', font=tkFont.Font(family='Lucida Grande', size=12, weight='bold'))
input_field.pack(ipady=4)
input_field.focus()
input_field.place(x=75, y=100)

# open `AddPathHere.txt` file to read the path(song location)
with open('AddPathHere.txt') as file:
	path = file.read().strip()

# function for searching and playing songs
def playSong():
	try:
		song = input_field.get().strip()
		for songs in os.listdir(path):
			if song in songs.lower():
				song_dir = os.path.join(path, songs)
				mp_3 = songs.endswith('mp4')
				mp_4 = songs.endswith('mp4')
				jpg = songs.endswith('jpg')
				if os.path.isfile(song_dir) and mp_3 or mp_4 or jpg:
					os.startfile(song_dir)
					input_field.delete(first=0, last=100)
		label['text'] = 'Enter any text you think is included in the song name'
	except FileNotFoundError:
		label['text'] = 'Check the path of your playlist if exists'
	except OSError:
		label['text'] = 'Check the permission or unlock the driver if is locked'


# function for picking random song and play it
def pickRandom():
	try:
		playList = [os.path.join(path, songs) for songs in os.listdir(path)]
		os.startfile(random.choice(playList))
		input_field.delete(first=0, last=100)
	except FileNotFoundError:
		label['text'] = 'Check the path of your playlist if exists'
	except OSError:
		label['text'] = 'Check the permission or unlock the driver if is locked'

random_button = Button(App, text="pick random", fg='white', bg='#6610f2', activebackground='#7710f2', width=9, height=1, bd=4, command=pickRandom, font=tkFont.Font(family='Lucida Grande', size=11, weight='bold'))
random_button.pack()
random_button.place(x=470, y=100)

# Button for search (submit)
search_button = Button(App, text="Search", fg='white', bg='#783ab7', activebackground='#984bb7', width=10, height=1, bd=4, command=playSong, font=fontStyle)
search_button.pack(ipady=5)
search_button.place(x=280, y=170)

# Trigger Enter key to run playSong()
input_field.bind('<Return>', lambda event: playSong())

# Button for reset
reset_button = Button(App, text="reset", fg='white', bg='#783ab7', activebackground='#984bb7', width=10, height=1, bd=4, font=fontStyle, command=lambda: input_field.delete(first=0, last=100))
reset_button.pack()
reset_button.place(x=150, y=170)

# Button for quit
quit_button = Button(App, text='Quit', fg='white', bg='#341e79', activebackground='#452e89', width=11, height=1, bd=4, command=App.destroy, font=fontStyle)
quit_button.pack()
quit_button.place(x=220, y=250)

# Trigger Escape<esc> key to destroy App
App.bind('<Escape>', lambda event: App.destroy())

# disable resizing
App.resizable(False, False)
App.mainloop()
