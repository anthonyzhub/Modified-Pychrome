from Settings import media_player, media_controller
from Media_Selection import list_contents, user_selection

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
    starter()
    contents.clear()
