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





