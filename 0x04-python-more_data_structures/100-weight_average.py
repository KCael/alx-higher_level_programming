#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    if (my_list and len(my_list) > 0):
        for (score, weight) in my_list:
            num += score * weight
            den += weight

    return (num / den)
