import pychromecast

# Locate any Google Devices connected to network
chromecasts = pychromecast.get_chromecasts()


def list_all_devices():
    """ This function will list all available devices within network. """

    # A list that will hold all names of available devices
    devices = {}
    x = 0

    print("\nList of all available devices:\n")

    # Add all available devices to dictionary
    for cc in chromecasts:
        devices[x] = cc.device.friendly_name
        x += 1

    # Display all devices available
    for key, value in devices.items():
        print('{}: {}'.format(key, value))

    # Ask user to pick a device
    print("\nSelect a device: ")
    user_device = input()

    # Check if input is valid
    while True:
        if int(user_device) in devices:
            return str(devices[int(user_device)])
        else:
            print("Sorry, {} is not listed.".format(str(user_device)))
            pass


x = list_all_devices()

# Of all the devices from 'chromecasts' look for user's specific device
cast = next(cc for cc in chromecasts if cc.device.friendly_name == x)

# Wait for device to be activated
cast.wait()

mc = cast.media_controller


def media_player(user_choice):
    """ This function will send media file to receiver. """

    path_with_video = "http://127.0.0.1/{}".format(user_choice)
    mc.play_media(path_with_video, content_type="video/mp3")
    mc.block_until_active()
    mc.play()


def media_controller():
    """ This function serves as a 'remote control' to the user. """

    # Infinite loop for user's response
    while True:
        actions = ['pause', 'play', 'stop']
        print("\nEnter action: {}".format(actions))
        user_input = input()

        if user_input == "pause":
            mc.pause()
            pass
        elif user_input == "play":
            mc.play()
            pass
        elif user_input == "stop":
            mc.stop()
            return 0
        else:
            print("Invalid choice: {}".format(str(user_input)))
