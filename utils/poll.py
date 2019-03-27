def numeric_metric(desired_metric, units, lobound, hibound):
    """Prompts user to provide a number 'desired_metric' with the units 'units'.
    Before returning user input, function validates number is in range using
    'lobound' and 'hibound' respectively.
    desired_metric -> string
    units -> string
    lobound -> string
    hibound -> string"""

    while True:
        # Poll user forever
        usr_input = raw_input('Enter your ' + desired_metric + ' (' + units + '): ')
        try:
            # Attempt to cast the input to an integer
            int(usr_input) == usr_input
        except:
            # If casting fails, print
            print('Entry non-numeric / out of range.\nTry again.')
        else:
            # return the input if it fits within the bounds
            if lobound < int(usr_input) < hibound and usr_input != str():
                return int(usr_input)
            else:
                # otherwise print an error
                print('Entry non-numeric / out of range.\nTry again.')


def alpha_metric(desired_metric, units):
    """Prompts user to provide a string 'desired_metric' with the units 'units'.
    Before returning user input, function validates input is a string.
    desired_metric -> string
    units -> string"""

    while True:
        # Poll user forever
        usr_input = raw_input('Enter your ' + desired_metric + ' (' + units + '): ')
        try:
            # Attempt to cast the input to a string
            str(usr_input) == usr_input
        except:
            # If casting fails, print
            print('Entry not a string.\nTry again.')
        else:
            # return the input if it matches the desired input
            if str(usr_input) == 'M' or 'F':
                return str(usr_input)
            else:
                # otherwise print an error
                print('Entry not a string.\nTry again.')
