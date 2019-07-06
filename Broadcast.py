import os
import socket
import sys
from pathlib import Path


class MediaPlayer:

    def __init__(self, cast_device_remote):

        """ Initializing this class requires the implementation of cast_device_remote """

        # List containing media files to cast
        self.media_list = []

        self.currentFilePlaying = ''

        # Control device's actions
        self.cast_remote = cast_device_remote

        # List of commands available during stream
        self.control_actions_dict = dict({
            'pause': self.cast_remote.pause,
            'stop': self.cast_remote.stop,
            'play': self.cast_remote.play,
            'restart video': self.cast_remote.rewind,
            #'next video': self.nextMediaFile,
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

        # Save name of file going to be played
        self.currentFilePlaying = play_file

        # Path file to media content
        file_path = 'http://{}:8000/{}'.format(ip_address, str(play_file.replace(" ", "%20")))
        print('path_file: {}'.format(file_path))

        # Play media file
        self.cast_remote.play_media(file_path, content_type='video/mp4')

        # Block access to device until media file ends
        self.cast_remote.block_until_active()

        # Play file
        self.cast_remote.play()

    def addMediaFiles(self):

        """ Filter files in directory, then add them to list """

        # Specify directory
        user_directory = '/Users/anthonyzamora/Movies/'

        counter = 1

        # Add playable files to list
        for item in os.listdir(user_directory):

            # Specifies item's path
            file_path = Path(user_directory + str(item))

            # Don't add hidden files or directories to list
            if (not item.startswith('.')) and file_path.is_file():

                # Add file to list
                self.media_list.append(item)

                # Print recently added file
                print('{}. {}'.format(counter, self.media_list[counter - 1]))
                counter += 1

    def chooseMediaFile(self):

        """ Allow user to pick a file """

        self.lineBreaker()

        while True:

            chosen_file = input('Pick a content to play ')

            if chosen_file.isdigit():

                # Get file from list
                # Subtracting 1 because the output list starts at 1, instead of 0
                temp = self.media_list[int(chosen_file) - 1]
                chosen_file = temp

                break

            elif chosen_file in self.media_list:

                break

            print('Sorry, wrong name or number')

        # Send cast file on device
        self.sendCastingFile(chosen_file)

    def nextMediaFile(self):

        """ Play next file on list, if user enters command  """

        # Check if file playing is the last element in list
        if self.currentFilePlaying == self.media_list[-1]:

            return "Sorry, you reached the end of the playlist. "
        else:

            # Locate position of current file being played
            counter = 0

            # Continue until reaching the end of the list
            for item in self.media_list:

                if item == self.currentFilePlaying:

                    # Send next file in list
                    self.sendCastingFile(self.media_list[counter + 1])

                # Increment counter
                counter += 1


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

