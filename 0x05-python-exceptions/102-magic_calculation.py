#!/usr/bin/python3
def magic_calculation(a, b):
    calc = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                calc += a ** b / i
        except Exception:
            calc = b + a
            break
    return calc
