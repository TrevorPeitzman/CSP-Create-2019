#---- I independently wrote all code from this line to line number 34 ----#

import utils.poll as poll
import utils.conversions as conversions
import time
import sys

typetime = .05

# Establish welcome message as a variable
intromessage = '\033[1;34;m Hello and welcome to MacroCalc. This program will inform you of your optimal daily levels' \
                '\nof nutritional macronutrients, vitamins, minerals, and hydration. First, we will ask you' \
                '\na few questions about yourself. Let us begin...\n \033[1;37;m'


def macrocalc():

    # Extra feature - the intromessage is "typed" on screen for added effect
    # I have extended the code found at https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    # Below, I have rewrote this code to be inline rather than its own function 
    # I also tuned the delay time in between each letter to better suit our needs 
    # and be easily accessible as its own varaiable
    for letter in intromessage:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(typetime)

    # using our created libraries and utilities, poll the user for their data
    age = poll.numeric_metric('age', 'years', 1, 100)
    height = poll.numeric_metric('height', 'inches', 24, 96)
    weight = poll.numeric_metric('weight', 'pounds', 80, 400)
    sex = poll.alpha_metric('gender', 'M/F')

#---- My collaborative partner wrote all code below this line ----#    
    
    # Once done polling, calculate and print the results
    print '\nYour BMI is: ' + str(round(conversions.bmi(height, weight), 2))
    print conversions.magnesium(age, sex)
    print conversions.calcium(age, sex)
    print conversions.potassium(age, sex)
    print conversions.sodium(age, sex)
    print 'Optimal Water Intake: ' + str(conversions.hydration(weight, age)) + ' liquid ounces/day'
    print '\n\033[1;34;m Thank you for using MacroCalc. Have a great day.'

    return


macrocalc()
