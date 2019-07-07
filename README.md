# Modified-Pychrome
A Modified Version of Pychromecast

**Prerequisites**:

1. Install `Pychromecast`
2. Use Python 3.4 interpreter
3. Have either a Google Home or Google Chromecast (any model) connected to the same network as your computer
4. Folder with media contents to stream

**Friendly Message**:

Hi All,

This program is built upon Pychromecast with additional features for any kind of user. It does not matter if you are a beginner or expert programmer, everyone is welcome to use it! 

Pychromecast was created by ballooob, who was generous to share their group's project to the Github community. His program allows users to access and stream personal content to their own Google devices. Feel free to check out his work (Link: https://github.com/balloob/pychromecast). 

Modified-Pychrome's main goal is to give an easy access to all computer scientist enthusiast, no matter the skill level, who would love to watch their homemade videos on their chromecast. Modified-Pychrome allow users to stream any media files from your computer to any Google device. Controlling the media content is available through an interactive console. Only minimal modifications are required in the program for all users. More details are available below.

Have fun streaming,

Anthony

**Instructions**:

1. Open `Terminal` and navigate to your media folder
2. Type and enter `python3 -m http.server` to start server
3. Open `Broadcast.py` and specify directory of the folder from Step 1 in `addMediaFiles()`. Save changes!
4. Execute `Main.py` in either Terminal or IDE
5. Select a Google device by either typing device's name or number associated with it
6. Similar to previous step, but involves in selecting a media file through an interactive console
7. The console will print out another message: `[pause, play, stop, terminate]`. These commands are similar to a remote of any T.V. However, `terminate` will stop the program from running internally. Enter any command, it is an interactive console
8. Sit back and relax!
