import os
from tkinter import *

App = Tk(className="Search Engine")
App.geometry("600x350")
App.configure(bg='green')

label = Label(text='Enter any text you think is included in the song name', width=100, height=2, fg='black', bg='lightgreen')
label.pack()

inputData = Entry(App, bd=5, width=50, fg='dodgerblue')
inputData.pack(side=LEFT)

path = '' # your song path here ex. Users/YourUserName/dir
def playSong():
	song = inputData.get().strip()
	for songs in os.listdir(path):
		if song in songs.lower():
			song_dir = os.path.join(path, songs)
			if os.path.isfile(song_dir) and songs.endswith('mp4'):
				os.startfile(song_dir)
				inputData.delete(first=0, last=100)

button = Button(App, text="Search", fg='white', bg='dodgerblue', activebackground='lightgreen', width=15, height=2, bd=4, command=playSong)
button.pack(side=RIGHT)

App.mainloop()
