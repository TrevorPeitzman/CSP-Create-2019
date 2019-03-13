
import utils.poll as poll
import utils.conversions as conversions

def macrocalc():

    age = poll.numeric_metric('age', 'years', 1, 100)
    height = poll.numeric_metric('height', 'inches', 24, 96)
    weight = poll.numeric_metric('weight', 'pounds', 80, 400)
    sex = poll.alpha_metric('gender', 'M/F')

    print conversions.bmi(height, weight)
    print (age, sex, weight)
    return


macrocalc()

