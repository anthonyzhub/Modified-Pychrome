import pychromecast


class SystemSettings:

    def __init__(self):

        """ Initializing this class requires the implementation of device_list and google_devices """

        self.device_list = []

        # Scan network for google devices
        self.google_devices = pychromecast.get_chromecasts()

    def lineBreaker(self):

        """ Function simply adds a new line """
        print("")

    def printDevicesInNetwork(self):

        """ Print all elements in device_list """

        counter = 1

        for item in self.device_list:
            print('{} - {}'.format(counter, item))

            counter += 1

    def appendLocalDevices(self):

        """ Function retrieves all google devices in local network"""

        # Append all devices available in network to list
        for item in self.google_devices:
            # Append device to dictionary
            self.device_list.append(item.device.friendly_name)

    def selectLocalDevice(self):

        """ Function checks if input is in network """

        self.printDevicesInNetwork()

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

                # Iterate through list
                for item in self.device_list:

                    # If user's choice == item in list
                    # exit loop
                    if device_selection == item:
                        break

            # Print if loop hasn't ended
            print("Sorry, wrong number or name.")

        # Return device
        return device_selection

    def connectToDevice(self, device_name):

        for device in self.google_devices:

            if device_name == device.device.friendly_name:
                # Wait until casting device is activated
                device.wait()

                # Return media controller
                return device.media_controller
