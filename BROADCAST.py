import os
import socket
import sys
import NODE
from pathlib import Path


class MediaPlayer:

    def __init__(self, cast_device_remote):

        """ Initializing this class requires the implementation of cast_device_remote """

        # List containing media files to cast
        self.media_list = []

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

        print("Goodbye, World...")
        sys.exit()

    def sendCastingFile(self, play_file):

        """ Sends media file to casting device """

        # Get ip address of this computer
        ip_address = socket.gethostbyname(socket.gethostname())

        # Path file to media content
        url_file_path = 'http://{}:8000/{}'.format(ip_address, str(play_file.replace(" ", "%20")))
        print('path_file: {}'.format(url_file_path))

        # Play media file
        self.cast_remote.play_media(url_file_path, content_type='video/mp4')

        # Block access to device until media file ends
        self.cast_remote.block_until_active()

        # Play file
        self.cast_remote.play()

    def addMediaFiles(self):

        user_directory = "/Users/anthonyzamora/Movies/"

        # Add playable files to list
        for item in os.listdir(user_directory):

            # Specifies item's path
            file_path = Path(user_directory + str(item))

            # Don't add hidden files or directories to list
            if (not item.startswith('.')) and file_path.is_file():

                # Add file to list
                self.nodeLinkedList.addNode(item)

        # Print link list
        self.nodeLinkedList.printList()

    def chooseMediaFile(self):

        self.lineBreaker()

        # Exit if linked list is empty
        if self.nodeLinkedList.isEmpty():
            print("NodeList is empty")
            return None

        # Create a temporary string variable to receive return value of getNodeElementBy*
        temp_str = ""

        # Keep loop running
        while True:

            # Ask for input
            chosen_file = input("Pick content to play: ")

            # If user entered digit, call getNodeByPosition()
            if chosen_file.isdigit():

                # Get file by position and make sure it isn't out of bound
                temp_str = self.nodeLinkedList.getNodeElementByPosition(int(chosen_file) - 1)

                # If None is not returned, then exit While loop
                if temp_str:
                    break

            elif not chosen_file.isdigit():

                # Get file by element's name and make sure it exists
                temp_str = self.nodeLinkedList.getNodeElementByName(chosen_file)

                if temp_str:
                    break

            else:
                # Execute if user's input doesn't exist
                print("{} does not exist".format(chosen_file))

        # If loop breaks, send choice of media file
        self.sendCastingFile(temp_str)

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
