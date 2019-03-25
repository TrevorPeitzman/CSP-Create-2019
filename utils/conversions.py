def bmi(height, weight):
    output = 703 * (float(weight)/(height**2))
    return float(output)


def hydration(weight, age):

    if age < 30:
        variable = 40
    elif age > 30 and age < 55:
        variable = 35
    else:
        variable = 30

    precursor = (float(weight / 2.2) * variable)
    output = (precursor / 28.3)
    return round(float(output), 2)


def calcium(age, sex):

    input = int(age)

    if input < 1:
        return 'Optimal Calcium: 260 mg'
    elif 1 <= input <= 3:
        return 'Optimal Calcium: 700 mg'
    elif 4 <= input <= 8:
        return 'Optimal Calcium: 1000 mg'
    elif 9 <= input <= 18:
        return 'Optimal Calcium: 1300 mg'
    elif 19 <= input <= 50:
        return 'Optimal Calcium: 1000 mg'
    elif 51 <= input <= 70:
        if sex == 'M':
            return 'Optimal Calcium: 1000 mg'
        else:
            return 'Optimal Calcium: 1200 mg'
    elif 71 <= input:
        return 'Optimal Calcium: 1200 mg'
    else:
        print 'calcium unknown'
        return 'calcium unknown'

def magnesium(age, sex):

    input = int(age)

    if input < 1:
        return 'Optimal Magnesium: 52.5 mg'
    elif 1 <= input <= 3:
        return 'Optimal Magnesium: 80 mg'
    elif 4 <= input <= 8:
        return 'Optimal Magnesium: 130 mg'
    elif 9 <= input <= 18:
        if sex == 'M':
            return 'Optimal Magnesium: 410 mg'
        else:
            return 'Optimal Magnesium: 360 mg'
    elif 19 <= input <= 50:
        return 'Optimal Magnesium: 410 mg'
    elif 51 <= input <= 70:
        if sex == 'M':
            return 'Optimal Magnesium: 410 mg'
        else:
            return 'Optimal Magnesium: 315 mg'
    elif 71 <= input:
        return 'Optimal Magnesium: 410 mg'
    else:
        print 'Optimal Magnesium unknown'
        return 'Optimal Magnesium unknown'

def potassium(age, sex):

    input = int(age)

    if input < 1:
        return 'Optimal Potassium: 630 mg'
    elif 1 <= input <= 3:
        return 'Optimal Potassium: 2,000 mg'
    elif 4 <= input <= 8:
        return 'Optimal Potassium: 2,300 mg'
    elif 9 <= input <= 13:
        if sex == 'M':
            return 'Optimal Potassium: 2,500 mg'
        else:
            return 'Optimal Potassium: 2,300 mg'
    elif 14 <= input <= 18:
        if sex == 'M':
            return 'Optimal Potassium: 3,000 mg'
        else:
            return 'Optimal Potassium: 2,300 mg'
    elif 19 <= input:
        if sex == 'M':
            return 'Optimal Potassium: 3,400 mg'
        else:
            return 'Optimal Potassium: 2,600 mg'
    else:
        print 'Optimal Potassium unknown'
        return 'Optimal Potassium unknown'

def sodium(age, sex):

    input = int(age)
    if input < 1:
        return 'Optimal Sodium: 550 mg'
    elif 1 <= input <= 3:
        return 'Optimal Sodium: 625 mg'
    elif 4 <= input <= 8:
        return 'Optimal Sodium: 925 mg'
    elif 9 <= input <= 18:
        return 'Optimal Sodium: 1300 mg'
    elif 19 <= input <= 50:
        return 'Optimal Sodium: 1000 mg'
    elif 51 <= input <= 70:
        if sex == 'M':
            return 'Optimal Sodium: 1000 mg'
        else:
            return 'Optimal Sodium: 1200 mg'
    elif 71 <= input:
        return 'Optimal Sodium: 1200 mg'
    else:
        print 'Optimal Sodium unknown'
        return 'Optimal Sodium unknown'


