from random import (
	randint,
	choice
)
import os
import click


# open `AddPathHere.txt` file to read the path(song location)
with open('AddPathHere.txt') as file:
	all_paths = file.read().strip().split('\n')

@click.group()
def manage():
	pass

for _path in all_paths:
	@manage.command()
	@click.argument("song")
	@click.option('-location', default=_path, help='Location of the song')
	def search(location, song):
		try:
			song = song.strip().lower()
			for songs in os.listdir(location):
				if song in songs.lower():
					song_dir = os.path.join(location, songs)
					mp_4 = songs.endswith('mp4')
					mp_3 = songs.endswith('mp3')
					mpg = songs.endswith('mpg')
					avi = songs.endswith('avi')
					if os.path.isfile(song_dir) and mp_4 or mp_3 or mpg or avi:
						os.startfile(song_dir)
		except FileNotFoundError:
			click.echo(click.style('Check the path of your playlist exists', fg='bright_red'))
		except OSError:
			click.echo(click.style('Check the path permission or unlock the driver if is locked', fg='bright_red'))


# in all_paths pick random path to search random song
random_path = all_paths[randint(0, len(all_paths) - 1)]

@manage.command()
@click.option('-location', default=random_path, help='Location of the song')
def random(location):
	try:
		playList = [os.path.join(random_path, songs) for songs in os.listdir(random_path)]
		os.startfile(choice(playList))
	except FileNotFoundError:
		click.echo(click.style('Check the path of your playlist exists', fg='bright_red'))
	except OSError:
		click.echo(click.style('Check the permission or unlock the driver if is locked', fg='bright_red'))

if __name__ == '__main__':
	manage()
