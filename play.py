import os
from tkinter import *
import tkinter.font as tkFont

App = Tk(className="Search")
App.iconbitmap('searchIcon.ico')
App.geometry("570x320")
App.configure(bg='#241e79')

fontStyle = tkFont.Font(family='Courier', size=13, weight='bold')

label = Label(text='Enter any text you think is included in the song name', width=100, height=2, fg='black', bg='#673ab7', font=fontStyle)
label.pack()

# an input field
inputData = Entry(App, bd=5, width=40, fg='dodgerblue', font=tkFont.Font(family='Lucida Grande', size=12, weight='bold'))
inputData.pack(ipady=4)
inputData.focus()
inputData.place(x=95, y=100)

# open `AddPathHere.txt` file to read the path(song location)
with open('AddPathHere.txt') as file:
	path = file.read().strip()

# function for searching and playing songs
def playSong():
	try:
		song = inputData.get().strip()
		for songs in os.listdir(path):
			if song in songs.lower():
				song_dir = os.path.join(path, songs)
				mp_3 = songs.endswith('mp4')
				mp_4 = songs.endswith('mp4')
				jpg = songs.endswith('jpg')
				if os.path.isfile(song_dir) and mp_3 or mp_4 or jpg:
					os.startfile(song_dir)
					inputData.delete(first=0, last=100)
		label['text'] = 'Enter any text you think is included in the song name'
	except FileNotFoundError:
		label['text'] = 'Check the path of your playlist exists'
	except OSError:
		label['text'] = 'Check the permission or unlock the driver if is locked'


# Button for search (submit)
search_button = Button(App, text="Search", fg='white', bg='#783ab7', activebackground='#984bb7', width=10, height=1, bd=4, command=playSong, font=fontStyle)
search_button.pack(ipady=5)
search_button.place(x=300, y=170)

# Trigger Enter key to run playSong()
inputData.bind('<Return>', lambda event: playSong())

# Button for reset
reset_button = Button(App, text="reset", fg='white', bg='#783ab7', activebackground='#984bb7', width=10, height=1, bd=4, font=fontStyle, command=lambda: inputData.delete(first=0, last=100))
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
