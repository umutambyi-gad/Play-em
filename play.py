import os
from tkinter import *
import tkinter.font as tkFont

App = Tk(className="Search")
App.geometry("600x350")
App.configure(bg='#5a05f1')

fontStyle = tkFont.Font(family='Courier', size=14, weight='bold')

label = Label(text='Enter any text you think is included in the song name', width=100, height=2, fg='black', bg='#056cf1', font=fontStyle)
label.pack()

inputData = Entry(App, bd=5, width=40, fg='dodgerblue', font=tkFont.Font(family='Lucida Grande', size=12, weight='bold'))
inputData.pack(side=LEFT, ipady=4)

with open('AddPathHere.txt') as file:
	path = file.read().strip()


def playSong():
	try:
		song = inputData.get().strip()
		for songs in os.listdir(path):
			if song in songs.lower():
				song_dir = os.path.join(path, songs)
				if os.path.isfile(song_dir) and songs.endswith('mp4'):
					os.startfile(song_dir)
					inputData.delete(first=0, last=100)
		label['text'] = 'Enter any text you think is included in the song name'
	except FileNotFoundError:
		label['text'] = 'Check the path of your playlist exists'
	except OSError:
		label['text'] = 'Check the permission or unlock the driver if is locked'



button = Button(App, text="Search", fg='white', bg='#179fca', activebackground='#197fda', width=10, height=1, bd=4, command=playSong, font=fontStyle)
button.pack(side=RIGHT, ipady=5)

App.resizable(False, False)
App.mainloop()
