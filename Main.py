from Settings import media_player, media_controller
from Media_Selection import list_contents, user_selection

"""
Check-list before running program

1. Open terminal with two tabs/windows
2. Select a directory to stream media contents
3. Enter 'python3 -m http.server' on terminal
4. On a different tab/window, locate this project's 'main.py' file.
5. Execute following command: 'python3 main.py'
6. Enjoy the movie!

P.S. Change default directory and media format in 'Media_Selection.py' and 'Settings.py'
"""


# Global variables
contents = dict()


def starter():
    """ This is the first function called when program starts. """

    # List contents in directory
    contents_copy = list_contents(contents)

    # Request user's choice
    user_choice = user_selection(contents_copy)

    # Prepare choice for transmission
    media_player(user_choice)

    # Control functions. Like a remote.
    if media_controller() == 0:
        pass


while True:
    """ Program's ignition """
    starter()
    contents.clear()
