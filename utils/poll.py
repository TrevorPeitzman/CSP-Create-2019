def numeric_metric(desired_metric, units, lobound, hibound):
    """Prompts user to provide a number 'desired_metric' with the units 'units'.
    Before returning user input, function validates number is in range using
    'lobound' and 'hibound' respectively.
    desired_metric -> string
    units -> string
    lobound -> string
    hibound -> string"""

    while True:
        usr_input = raw_input('Enter your ' + desired_metric + ' (' + units + '): ')
        try:
            int(usr_input) == usr_input
        except:
            print('Entry non-numeric / out of range.\nTry again.')
        else:
            if lobound < int(usr_input) < hibound and usr_input != str():
                return int(usr_input)
            else:
                print('Entry non-numeric / out of range.\nTry again.')


def alpha_metric(desired_metric, units):
    """Prompts user to provide a string 'desired_metric' with the units 'units'.
    Before returning user input, function validates input is a string.
    desired_metric -> string
    units -> string"""

    while True:
        usr_input = raw_input('Enter your ' + desired_metric + ' (' + units + '): ')
        try:
            str(usr_input) == usr_input
        except:
            print('Entry not a string.\nTry again.')
        else:
            if str(usr_input) == 'M' or 'F':
                return str(usr_input)
            else:
                print('Entry not a string.\nTry again.')
