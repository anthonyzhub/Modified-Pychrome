import pychromecast


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

    def addDevicesToList(self):

        """ Function retrieves all google devices in local network"""

        counter = 1

        for device in self.google_devices:

            # Adds devices' name to list
            self.device_list.append(device.device.friendly_name)

            # Prints list
            print('{} - {}'.format(counter, self.device_list[counter - 1]))
            counter += 1

    def selectLocalDevice(self):

        """ Function checks if input is in network """

        # Keep in while loop until user selects correct device
        while True:

            # Adds an empty line in terminal
            self.lineBreaker()

            # Ask user for selection
            device_selection = input("Select device from list above: ")

            if device_selection.isdigit():

                # Create temp variable to hold value
                # Subtracting 1 because the output list starts at 1, instead of 0
                temp = self.device_list[int(device_selection) - 1]

                # Copy and past value to device_selection
                device_selection = temp

                # exit loop
                break

            else:

                if device_selection in self.device_list:
                    break

            # Print if loop hasn't ended
            print("Sorry, wrong number or name.")

        # Return device
        return device_selection

    def connectToDevice(self, device_name):

        """ Go through all elements in list, until 'friendly_name' and 'device_name" matches"""

        for device in self.google_devices:

            if device_name == device.device.friendly_name:
                # Wait until casting device is activated
                device.wait()

                # Return media controller
                return device.media_controller

