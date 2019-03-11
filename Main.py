import Broadcast
import System


def main():

    # Create instance for SystemSettings
    system_settings = System.SystemSettings()

    # Search device in network, then add to device_list
    system_settings.appendLocalDevices()

    # Save user's device choice
    device_name = system_settings.selectLocalDevice()

    # Look for the device in google_devices and connect to it
    cast_device = system_settings.connectToDevice(device_name)

    # Create instance of MediaPlayer class to control what to play
    media_player = Broadcast.MediaPlayer(cast_device)

    # Add media files to list
    media_player.addMediaFiles()

    # Allow user to select streaming file
    media_player.chooseMediaFile()

    # Give user the 'remote' to control the device (ex. pause, play, stop)
    media_player.remoteControlForDevice()


main()
