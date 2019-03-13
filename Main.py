
import utils.poll as poll
import utils.conversions as conversions
import time
import sys

intromessage = '\033[1;34;m Hello and welcome to MacroCalc. This program will inform you of your optimal levels of' \
                '\nnutritional macronutrients, vitamins, minerals, and hydration. First, we will begin by asking you' \
                '\na few questions about yourself. Let us begin...\n \033[1;37;m'

def macrocalc():

    for letter in intromessage:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.05)

    age = poll.numeric_metric('age', 'years', 1, 100)
    height = poll.numeric_metric('height', 'inches', 24, 96)
    weight = poll.numeric_metric('weight', 'pounds', 80, 400)
    sex = poll.alpha_metric('gender', 'M/F')

    print 'Your BMI is: ' + str(round(conversions.bmi(height, weight), 2))
    print (age, sex, weight)
    return


macrocalc()

