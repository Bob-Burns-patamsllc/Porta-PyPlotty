
## conversion factors


##mm to pixel
def milim_convert(input):
    output = input *  0.2645833333

    return float(output)

##micron to pixel
def microm_convert(input):
    output = input *  0.0002645833333

    return float(output)

##mil to pixel
def mil_convert(input):
    output = input * 0.096

    return float(output)

##inches to pixel
def inch_convert(input):
    output = input * 96.0

    return float(output)