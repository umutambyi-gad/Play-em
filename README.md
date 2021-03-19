# Play 'em
***a script for searching and playing songs from different location on your computer.***<br><br>
This script will give you GUI app which has an input field and search button where you will enter some phrase in the input field that you think is included in specific song and click on search button then the script will look up in your playlist location and opens it or click pick random button to place random song.<br>
This will reduce the time you spend while you're looking into your playlist to search for one song to play.<br>
And also if many songs matches all of them will be played in your default media player.
# Author
[***Umutambyi Gad***](https://umutambyigad.herokuapp.com)
# Usage
When you alread done with requirements just add the location<small>(path)</small> of where playlist is located on the [`AddPathHere.txt`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/AddPathHere.txt) file like the following notice that you should just add only one path.
```text
C:\Users\UserName\Songs
```
***or add multiple paths like:***
```text
C:\Users\UserName\Songs\new school
C:\Users\UserName\Songs\old school
```


## Thereafter there are two ways to run the script
**1. to run it with GUI app**


run [`play.py`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/play.py) in your command line or execute it in your *favorite editor/IDE*.


**OR**


edit [`run.bat`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/run.bat) to inlcude the path of your python script's path just see an example bellow.

```batch
@echo off
python C:/UserName/YourPythonScriptLocated/play.py #this line 
```
**Thereafter double click on `run.bat` batch file**

---

**After running the script then you will see GUI app Like**

![GUI App](https://user-images.githubusercontent.com/65312850/99289510-5a6ad900-283d-11eb-80e3-206bdffce65b.PNG)

**Then type the song that you want to play and hit Enter or click on search button to play that song**

![Playing song](https://user-images.githubusercontent.com/65312850/99182957-b3047e00-2738-11eb-95ad-d8b7514d43fb.PNG)

***Another cool thing***
You can click on `pick random`  or <kbd>ctrl</kbd> + <kbd>r</kbd> on keyboard button to play random song.


**2. to run it from the command line**


Just run python script [`playUsingCommandLine.py`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/playUsingCommandLine.py) I created with the help of [click](https://pypi.org/project/click/) module which will be executed in the command line.

**Syntax**

```bash
python  playUsingCommandLine.py [OPTIONS] COMMAND [ARGS]
```
[OPTIONS] is by default the path wich is written on [`AddPathHere.txt`](https://github.com/umutambyi-gad/Play-my-songs/blob/master/AddPathHere.txt) file so to run it just do it like the following.

```bash
python playUsingCommandLine.py search godzil
```
**Or pick random**
```bash
python playUsingCommandLine.py random
```
