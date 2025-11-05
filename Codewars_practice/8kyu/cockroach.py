import random

s = random.randint(1,25)

def cockroach_speed(s):
    import math
    cm = s / 0.036
    return(math.floor(cm))

cockroach_speed(s)