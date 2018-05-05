import os


def list_contents(contents):
    """ This function locates and prints directory. """

    # Specify directory
    directory = '/Users/Movies/'

    # Counter for 'for-loop'
    x = 0

    # Add all contents in list
    for file in os.listdir(directory):
        contents[x] = file
        x += 1

    # Print dictionary
    for key, value in contents.items():
        print("{}: {}".format(key, value))

    return contents


def user_selection(contents):
    """ This function asks for user to select media content. """

    while True:
        print('\nEnter number associated with media content: ')
        user_input = input()

        if int(user_input) in contents:
            return str(contents[int(user_input)])
        else:
            print('{} is not available'.format(user_input))