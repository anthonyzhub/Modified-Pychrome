import BROADCAST
import SYSTEM


def main():

    # Create instance for SystemSettings
    system_settings = SYSTEM.SystemSettings()

    # Search device in network, then add to device_list
    system_settings.addDevicesToList()

    # Save user's device choice
    device_chosen = system_settings.selectLocalDevice()

    # Create instance of MediaPlayer class to control what to play
    media_player = BROADCAST.MediaPlayer(device_chosen)

    # Add media files to list
    media_player.addMediaFiles()

    # Allow user to select streaming file
    media_player.chooseMediaFile()

    # Give user the 'remote' to control the device (ex. pause, play, stop)
    media_player.remoteControlForDevice()


main()
