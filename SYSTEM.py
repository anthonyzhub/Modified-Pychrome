import pychromecast
import sys


class SystemSettings:

    def __init__(self):

        """ Initializing this class requires the implementation of device_list and google_devices """

        self.device_list = []

        # Scan network for google devices
        self.google_devices = pychromecast.get_chromecasts()

    @staticmethod
    def lineBreaker():

        """ Function simply adds a new line """
        print("")

    def isDeviceFound(self):

        if not self.google_devices:
            print("No devices were found in network. Goodbye")
            sys.exit()

    def addDevicesToList(self):

        """ Prints network devices"""

        counter = 1

        for device in self.google_devices:

            # Adds devices' name to list
            self.device_list.append(device.device.friendly_name)

            # Prints list
            print('{} - {}'.format(counter, self.device_list[counter - 1]))
            counter += 1

    def selectLocalDevice(self):

        """ Asks user for device selection and connects to it """

        # Keep in while loop until user selects correct device
        while True:

            # Adds an empty line in terminal
            self.lineBreaker()

            # Ask user for selection
            device_selection = input("Select a device: ")

            if device_selection.isdigit():

                # Create temp variable to hold value
                # Subtracting 1 because the output list starts at 1, instead of 0
                temp = self.device_list[int(device_selection) - 1]

                # Copy and past value to device_selection
                device_selection = temp

                # exit loop
                break

            else:

                # If a string is entered, check if it exists in list
                # This simply checks if the name is spelled correctly
                if device_selection in self.device_list:
                    break

            # Print if nothing was found
            print("Sorry, wrong number or name.")

        # After locating the correct device, connect to it
        for device in self.google_devices:

            if device_selection == device.device.friendly_name:

                # Wait until casting device is activated
                device.wait()

                # Return media controller
                return device.media_controller
