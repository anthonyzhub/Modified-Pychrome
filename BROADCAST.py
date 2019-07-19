import os
import socket
import sys
import NODE
from pathlib import Path


class MediaPlayer:

    def __init__(self, cast_device_remote):

        """ Initializing this class requires the implementation of cast_device_remote """

        # Linked list containing media files to castz
        self.nodeLinkedList = NODE.DoubleLinkedList()

        # Control device's actions
        self.cast_remote = cast_device_remote

        # List of commands available during stream
        self.control_actions_dict = dict({
            'pause': self.cast_remote.pause,
            'stop': self.cast_remote.stop,
            'play': self.cast_remote.play,
            'restart video': self.cast_remote.rewind,
            'change video': self.chooseMediaFile,
            'terminate': self.terminateProgram,
            'enable subtitles': self.cast_remote.enable_subtitle,
            'disable subtitles': self.cast_remote.disable_subtitle
        })

    @staticmethod
    def lineBreaker():

        """ Function simply adds a new line """
        print("")

    def terminateProgram(self):

        """ Terminate, or Quit, program from running """
        self.lineBreaker()

        # Stop file from playing
        self.cast_remote.stop()
        print("Goodbye, World...")

        # Terminate program
        sys.exit()

    def sendFileToCast(self, play_file, online_video_link=False):

        """ Sends media file to casting device """

        # Get ip address of this computer
        ip_address = socket.gethostbyname(socket.gethostname())

        if not online_video_link:
            # Path file to media content
            url_file_path = 'http://{}:8000/{}'.format(ip_address, str(play_file.replace(" ", "%20")))
            print('path_file: {}'.format(url_file_path))

        else:
            url_file_path = play_file

        # Play media file
        self.cast_remote.play_media(url_file_path, content_type='video/mp4')

        # Block access to device until media file ends
        self.cast_remote.block_until_active()

        # Play file
        self.cast_remote.play()

    def addMediaFiles(self):

        # Merge current working directory with file name
        settings_text_path = os.path.join(os.getcwd(), "SETTINGS.txt")

        # If file exists, then open it
        if os.path.exists(settings_text_path):
            with open("SETTINGS.txt", "r") as settings_file:

                # Read text file
                data = settings_file.readlines()

                # Return 1st line of text and remove "media_directory = "
                get_path = data[0]
                media_directory_path = get_path.split("media_directory= ")[1]

                # Add playable files to list
                for item in os.listdir(media_directory_path):

                    # Specifies item's path
                    file_path = Path(media_directory_path + str(item))

                    # Don't add hidden files or directories to list
                    if (not item.startswith('.')) and file_path.is_file():

                        # Add file to list
                        self.nodeLinkedList.addNode(item)

                # Print link list
                self.nodeLinkedList.printLinkedList()

        else:

            # Print if path doesn't exist
            print("{} does not exist".format(settings_text_path))

    def chooseMediaFile(self):

        self.lineBreaker()

        # Exit if linked list is empty
        if self.nodeLinkedList.isEmpty():
            alternative_choice = input("Media folder is empty. Would you like to stream an online video? Y/n")

            if alternative_choice == "Y" or alternative_choice == "y":
                video_link = input("Enter URL link: ")
                self.sendFileToCast(video_link, online_video_link=True)

            else:
                return None

        # Keep loop running
        while True:

            # Ask for input
            chosen_file = input("File/URL to Play: ")

            input_is_url = False
            file_exists = False

            # Check if input is a URL link
            if chosen_file.startswith("http"):
                input_is_url = True
                break

            # If user entered digit, call getNodeByPosition()
            elif chosen_file.isdigit():
                # Get file by position and make sure it isn't out of bound
                if self.nodeLinkedList.getNodeElementByPosition(int(chosen_file) - 1):
                    file_exists = True
                    break

            elif not chosen_file.isdigit():
                # Get file by element's name and make sure it exists
                if self.nodeLinkedList.getNodeElementByName(chosen_file):
                    file_exists = True
                    break

            else:
                # Execute if user's input doesn't exist
                print("{} does not exist".format(chosen_file))

        # If loop breaks, set proper parameters
        if input_is_url:
            self.sendFileToCast(chosen_file, online_video_link=True)
        elif file_exists:
            self.sendFileToCast(chosen_file)

    def remoteControlForDevice(self):

        """ Function serves as a remote control for video play """

        # Keep function active by creating while loop
        while True:

            self.lineBreaker()

            # Prints available commands
            counter = 1
            for action in self.control_actions_dict.keys():
                print('{}. {}'.format(counter, action))
                counter += 1

            # Request input and makes string lowercase
            action_selected = input("Enter Command: ")
            action_selected.lower()

            # Check if input is a key
            if action_selected in self.control_actions_dict.keys():

                # Execute program
                self.control_actions_dict[action_selected]()

            else:
                print("Sorry, invalid command. ")
