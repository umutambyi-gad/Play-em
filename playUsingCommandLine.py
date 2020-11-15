import os
import click

# open `AddPathHere.txt` file to read the path(song location)
with open('AddPathHere.txt') as file:
	path = file.read().strip()

@click.command()
@click.argument("song")
@click.option('-location', default=path, help='Location of the song')
def search(location, song):
	try:
		song = song.strip().lower()
		for songs in os.listdir(location):
			if song in songs.lower():
				song_dir = os.path.join(location, songs)
				if os.path.isfile(song_dir) and songs.endswith('mp4'):
					os.startfile(song_dir)
	except FileNotFoundError:
		click.echo(click.style('Check the path of your playlist exists', fg='bright_red'))
	except OSError:
		click.echo(click.style('Check the permission or unlock the driver if is locked', fg='bright_red'))

if __name__ == '__main__':
	search()
