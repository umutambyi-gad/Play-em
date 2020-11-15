# Python script for play songs from local playlist
This script will give you GUI app which has input field and button where you will enter some text in the input field that you think is included in specific song and click on search button then the script will look up in your playlist location and opens it.<br>
This will reduce the time you spend while you're looking into your playlist to search for one song to play.<br>
And also if many songs matches all of them will be place in your default media player

## Getting started
First of all install python version 3 and all requirements like the following to get started 
```python
pip install -r requirements.txt #on windows
#OR
pip3 install -r requirements.txt #on MAC OS and Linux
```

## Usage
When you alread done with requirements just add the location<small>(path)</small> of where your playlist is located on `AddPathHere.txt` file like the following notice that you should just add only one path.
```
C:\Users\UserName\Songs
```
**Thereafter there are two ways to run the script**
- to run `play.py` in your command line or execute it in your *favorite editor/IDE* here is how in the command line

```python
python play.py #on windows
#OR
python3 play.py #on MAC OS and Linux
```
- edit `run.bat` to inlcude the path of your python script's path just see an example bellow **Thereafter double click on `run.bat` batch file**

```batch
@echo off
python C:/UserName/YourPythonScriptLocated/play.py #this line 
```


---
**After running the script then you will see GUI app Like**

![GUI App](https://user-images.githubusercontent.com/65312850/99182949-a97b1600-2738-11eb-83d8-fa4bdb77a227.PNG)

**Then type the song that you want to play and hit search button to play that song**

![Playing song](https://user-images.githubusercontent.com/65312850/99182957-b3047e00-2738-11eb-95ad-d8b7514d43fb.PNG)

## RECOMANDATION

To make it easier I recomanded to set an envirement variable of the location of the script in order to run the script wherever you're on your computer by running the batch file called `run.bat` like

![Run bat](https://user-images.githubusercontent.com/65312850/99182943-9f591780-2738-11eb-818c-5103d1ba9dbb.PNG)

## UPDATE
I just added python script <small>`playUsingCommandLine.py`</small> with the help of [click]()
module which will be run in the command line.


Syntax

```bash
python  playUsingCommandLine.py [OPTIONS] SONG
```
[OPTIONS] is by default the path wich is written on `AddPathHere.txt` file
so to run it just do it like the following.

```python
python playUsingCommandLine.py godzil...
```