import pychromecast
import sys
import os


class SystemSettings:

    def __init__(self):

        """ Initializing this class requires the implementation of device_list and google_devices """

        self.device_map = {}

        # Scan network for google devices
        self.google_devices = pychromecast.get_chromecasts()

    @staticmethod
    def lineBreaker():

        """ Function simply adds a new line """
        print("")

    def printDictionary(self, dict_1):

        for key, value in dict_1.items():
            print("{} - {}".format(key, value))

    def isDeviceFound(self):

        """ Exit program if no casting devices were found"""

        if not self.google_devices:
            print("No devices were found in network. Goodbye")
            sys.exit()

    def isSettingsFileFound(self):

        # Get current working directory and merge it with file name
        settings_path = os.path.join(os.getcwd(), "SETTINGS.txt")

        # Check if file exists in current directory
        if not (os.path.exists(settings_path)):
            print("SETTINGS.txt does not exist")

            # Ask user which folder has media files to cast
            while True:

                print("Enter path of folder with media files to cast. It is CASE SENSITIVE. ")
                media_directory = input("Case Sensitive Path: ")

                # If it doesn't end with "/", program will look for another file
                if media_directory[-1] is not "/":
                    media_directory = media_directory + "/"

                if os.path.exists(media_directory):

                    # Create SETTINGS.txt and store user's media directory
                    file_to_create = open("SETTINGS.txt", "w+")
                    file_to_create.write("media_directory= " + media_directory)
                    file_to_create.close()

                    break
                else:
                    print("Sorry, directory doesn't exist. Try again")

    def addDevicesToList(self):

        # Iterate google_devices list
        for local_network_device in self.google_devices:

            # Add friendly_name as key, and all information as value to dictionary
            self.device_map[local_network_device.device.friendly_name] = local_network_device

    def selectLocalDevice(self):

        # Create list that will hold all devices' information
        temp_device_list = []

        # Print dictionary
        counter = 1
        for key in self.device_map.keys():
            print("{} - {}".format(counter, key))
            temp_device_list.append(self.device_map[key])
            counter += 1

        while True:

            device_selected = input("Select a device: ")

            # Check if device exist by checking if it is a key
            if device_selected in self.device_map.keys():

                # Wait for device to respond
                self.device_map[device_selected].wait()

                # Return device's controls
                return self.device_map[device_selected].media_controller

            # Check if input is a digit and length is less than temp_device_list
            elif device_selected.isdigit() and (int(device_selected) - 1) <= len(temp_device_list):
                temp_device_list[int(device_selected) - 1].wait()

                return temp_device_list[int(device_selected) - 1].media_controller

            else:
                print("Device not found")
