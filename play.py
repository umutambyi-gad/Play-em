import tkinter.font as tkFont
import os
from tkinter import (
	Tk,
	Label,
	Entry,
	Button
)
from random import (
	randint,
	choice
)
import platform
import subprocess

App = Tk(className="Search")
if platform.system() == "Windows":
	App.iconbitmap('searchIcon.ico')
App.geometry("590x330")
App.configure(bg='#241e79')

fontStyle = tkFont.Font(family='Courier', size=13, weight='bold')

label = Label(text='Enter any text you think is included in the song name', width=100, height=2, fg='white', bg='#673ab7', font=fontStyle)
label.pack()

# an input field
input_field = Entry(App, bd=5, width=40, fg='dodgerblue', font=tkFont.Font(family='Lucida Grande', size=12, weight='bold'))
input_field.pack(ipady=4)
input_field.focus()
input_field.place(x=75, y=100)

# open `AddPathHere.txt` file to read the path(song location)
with open('AddPathHere.txt') as file:
	all_paths = file.read().strip().split('\n')

# function for searching and playing songs
def playSong():
	try:
		song = input_field.get().strip()
		for _path in all_paths:
			for songs in os.listdir(_path):
				if song.lower() in songs.lower():
					song_dir = os.path.join(_path, songs)
					mp_3 = songs.endswith('mp3')
					mp_4 = songs.endswith('mp4')
					mpg = songs.endswith('mpg')
					avi = songs.endswith('avi')
					if os.path.isfile(song_dir) and mp_3 or mp_4 or mpg or avi:
						if platform.system() == 'Windows':
							os.startfile(song_dir)
						else:
							subprocess.call(['open', song_dir])
						input_field.delete(first=0, last=100)
			label['text'] = 'Enter any text you think is included in the song name'
	except FileNotFoundError:
		label['text'] = 'Check the path of your playlist if exists'
		label['fg'] = 'red'
	except OSError:
		label['text'] = 'Check the permission or unlock the driver if it is locked'
		label['fg'] = 'red'


# function for picking random song and play it
def pickRandom():
	try:
		query = input_field.get().strip()
		# in all_paths pick random path to search random song
		random_path = all_paths[randint(0, len(all_paths) - 1)]
		if query:

			playList = [os.path.join(random_path, songs) for songs in os.listdir(random_path) if query.lower() in songs.lower()]
			if platform.system() == 'Windows':
				os.startfile(playList)
			else:
				subprocess.call(['open', choice(playList)])
		else:
			playList = [os.path.join(random_path, songs) for songs in os.listdir(random_path)]
			if platform.system() == 'Windows':
				os.startfile(choice(playList))
			else:
				subprocess.call(['open', choice(playList)])
		input_field.delete(first=0, last=100)
	except FileNotFoundError:
		label['text'] = 'Check the path of your playlist if exists'
		label['fg'] = 'red'
	except OSError:
		label['text'] = 'Check the permission or unlock the driver if it is locked'
		label['fg'] = 'red'

random_button = Button(App, text="pick random", fg='white', bg='#6610f2', activebackground='#7710f2', width=9, height=1, bd=4, command=pickRandom, font=tkFont.Font(family='Lucida Grande', size=11, weight='bold'))
random_button.pack()
random_button.place(x=470, y=100)

# Trigger r key to run pickRandom()
input_field.bind('<Control-r>', lambda event: pickRandom())

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
