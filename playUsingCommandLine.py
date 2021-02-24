from random import choice
from os import (
	listdir,
	path,
	startfile
)
import click


# open `AddPathHere.txt` file to read the path(song location)
with open('AddPathHere.txt') as file:
	file_path = file.read().strip()

@click.group()
def manage():
	pass

@manage.command()
@click.argument("song")
@click.option('-location', default=file_path, help='Location of the song')
def searchSong(location, song):
	try:
		song = song.strip().lower()
		for songs in listdir(location):
			if song in songs.lower():
				song_dir = path.join(location, songs)
				if path.isfile(song_dir) and songs.endswith('mp4') or songs.endswith('mp3'):
					startfile(song_dir)
	except FileNotFoundError:
		click.echo(click.style('Check the path of your playlist exists', fg='bright_red'))
	except OSError:
		click.echo(click.style('Check the permission or unlock the driver if is locked', fg='bright_red'))

@manage.command()
@click.option('-location', default=file_path, help='Location of the song')
def pickRandom(location):
	try:
		playList = [path.join(file_path, songs) for songs in listdir(file_path)]
		startfile(choice(playList))
	except FileNotFoundError:
		click.echo(click.style('Check the path of your playlist exists', fg='bright_red'))
	except OSError:
		click.echo(click.style('Check the permission or unlock the driver if is locked', fg='bright_red'))

if __name__ == '__main__':
	manage()
