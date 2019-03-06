import os
import socket
import sys


class MediaPlayer:

    def __init__(self, cast_device_remote):

        """ Initializing this class requires the implementation of cast_device_remote """

        self.media_list = []
        self.cast_remote = cast_device_remote

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

        file_path = 'http://{}:8000/{}'.format(ip_address, str(play_file.replace(" ", "%20")))
        print('path_file: {}'.format(file_path))

        # Play media file
        self.cast_remote.play_media(file_path, content_type='video/mp4')

        # Block access to device until media file ends
        self.cast_remote.block_until_active()

        # Play file
        self.cast_remote.play()

    def printMediaList(self):

        """ Print elements in media_list"""

        counter = 1

        for item in self.media_list:
            print('{}. {}'.format(counter, item))

            counter += 1

    def addMediaFiles(self):

        """ Display all files that are playable in Chromecast """

        # Specify directory
        user_directory = '/Users/anthonyzamora/Movies/'

        # Add playable files to list
        for file in os.listdir(user_directory):

            # Don't add any files starting with '.'
            if not file.startswith('.'):
                self.media_list.append(file)

        # Sort list in alphabetical order
        self.media_list.sort()

        # Print list
        self.printMediaList()

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

                # Play file
                self.sendCastingFile(chosen_file)

                break

            elif chosen_file in self.media_list:

                # Play file
                self.sendCastingFile(chosen_file)

                break

            print('Sorry, wrong name or number')

    def remoteControlForDevice(self):

        """ Function serves as a remote control for video play """
        control_actions = ['pause', 'play', 'stop', 'terminate']

        # Print list
        print(control_actions)

        # Keep function active by creating while loop
        while True:

            self.lineBreaker()

            # Request input and make string lowercase
            action_selected = input("Select Command from above: ")
            action_selected.lower()

            # Look for requested action
            if action_selected == 'pause':
                self.cast_remote.pause()
            elif action_selected == 'play':
                self.cast_remote.play()
            elif action_selected == 'stop':

                """
                What does this condition do?
                
                1. It stops file from playing
                2. Overrides 'action_selected' to ask the user for their choice
                3. If it continues to play, it'll be exited from the outer 'if' condition
                4. If user chooses another file, it wil print available options, select another file, and continue
                    in the while-loop
                5. It will terminate, or quit, the program with a nice message
                """

                # First, stop file from play
                self.cast_remote.stop()

                # Ask user to continue playing video or to select another
                action_selected = input("Should I 'play' file, choose 'another' file, or 'terminate' program? ")
                action_selected.lower()

                # Continue playing the video
                if action_selected == 'play':

                    # Exit outer 'if' condition without any changes
                    continue

                elif action_selected == 'another':

                    self.lineBreaker()

                    # Show other options
                    self.printMediaList()

                    # Let user pick another file to play
                    self.chooseMediaFile()

                elif action_selected == 'terminate':

                    self.terminateProgram()

            elif action_selected == 'terminate':

                self.terminateProgram()
            else:
                print("Sorry, invalid command")
