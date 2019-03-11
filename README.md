# Modified-Pychrome
A Personal Modified Version of Pychromecast

**Prerequisites**:

1. Install and update `Pychromecast`
2. Python 3.4
3. Either a Google Home or Google Chromecast (any model)
4. Folder with files to stream
5. Computer and Google device must be in the same network
6. Friendly Message

Hi All,

This program is built upon Pychromecast with additional features for any kind of user. It does not matter if you are a beginner or expert programmer. Everyone is welcomed to use it! 

Pychromecast was created by ballooob, who is generous to share their group's project to the Github community. It allows users to access and stream personal content to the user's Google devices. Feel free to check out their work (Link: https://github.com/balloob/pychromecast). 

My main goal is to give an easy access to all computer scientist enthusiat, no matter the skill level, who would love to watch their homemade videos on their chromecast.

Modified-Pychrome allows you to stream any media files from your computer to either a Chromecast or a Home device. Controlling
the media content is available through an interactive console. Only minimal modifications are required in the python files for all users. 

Before running and compiling this program, please set your directory (the folder you want to stream from) in the python script.

Have fun streaming,

Anthony

**Instructions**:

1. Open `Terminal` and navigate to the folder with the files you want to stream
2. Type and enter `python3 -m http.server`
3. Open Broadcast.py and specify directory of the folder from Step 1 in `addMediaFiles()`. Save changes!
4. Execute `Main.py` in either Terminal or IDE
5. Select Google device by either typing name or number associated with it
6. Similar to previous step, but with media files
7. The console will print out another message: `[pause, play, stop, terminate]`. These commands are similar to a remote of any T.V.
  However, `terminate` will stop the program from running internally. Enter any command, it is an interactive console
8. Sit back and relax!
