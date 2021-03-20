# Play 'em
***python GUI and command line utility for searching and playing songs from different location on your computer.***<br><br>
This script will give you GUI app which has an input field and search button where you will enter some phrase in the input field that you think is included in specific song and click on search button then the script will look up in your playlist location and opens it or click pick random button to place random song.<br>
This will reduce the time you spend while you're looking into your playlist to search for one song to play.<br>
And also if many songs matches all of them will be played in your default media player.
# Author
**Website:** [umutambyigad](https://umutambyigad.herokuapp.com) <br>
**Stackoverflow:** [@umutambyi-gad](https://stackoverflow.com/users/13536893/umutambyi-gad) <br>
**Twitter:** [@umutambyi_gad](https://twitter.com/umutambyi_gad) <br>
**Linkedin:**  [@umutambyi-gad](https://www.linkedin.com/in/umutambyi-gad/) <br>
**Dev.to:** [@umutambyigad](https://dev.to/umutambyigad) <br>
**Email:** [umutambyig@gmail.com](mailto:umutambyig@gmail.com) <br>

# Usage
When you alread done with requirements just add the location<small>(path)</small> of where playlist is located on the [`AddPathHere.txt`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/AddPathHere.txt) file like the following.
```text
C:\Users\UserName\Songs
```
***or add multiple paths like:***
```text
C:\Users\UserName\Songs\new school
C:\Users\UserName\Songs\old school
```


## Thereafter there are two ways to run the script
### 1. to run it with GUI app


run [`play.py`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/play.py) via command line or execute it via your *favorite editor/IDE*.

**After running the script then you will see GUI app Like**

![GUI App](https://user-images.githubusercontent.com/65312850/99289510-5a6ad900-283d-11eb-80e3-206bdffce65b.PNG)

**Then type the song that you want to play and hit Enter or click on search button to play that song**

![Playing song](https://user-images.githubusercontent.com/65312850/99182957-b3047e00-2738-11eb-95ad-d8b7514d43fb.PNG)

***Another cool thing***
You can click on `pick random`  or <kbd>ctrl</kbd> + <kbd>r</kbd> on keyboard button to play random song.


### 2. to run it from the command line


Just run [`playUsingCommandLine.py`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/playUsingCommandLine.py)

**Syntax**

```bash
python  playUsingCommandLine.py [OPTIONS] COMMAND [ARGS]
```

**Example**

```bash
python playUsingCommandLine.py search godzil
```
**Or pick random**

```bash
python playUsingCommandLine.py random
```
