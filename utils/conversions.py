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
        return '260 mg'
    elif 1 <= input <= 3:
        return '700 mg'
    elif 4 <= input <= 8:
        return '1000 mg'
    elif 9 <= input <= 18:
        return '1300 mg'
    elif 19 <= input <= 50:
        return '1000 mg'
    elif 51 <= input <= 70:
        if sex == 'M':
            return '1000 mg'
        else:
            return '1200 mg'
    elif 71 <= input:
        return '1200 mg'
    else:
        print 'calcium unknown'
        return 'calcium unknown'



