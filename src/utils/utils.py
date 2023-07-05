import numpy as np


def quantize_leo(line):
    """
    Quantize leo code according to the data
    inputs: One line data
    return: fixed_number, is_negative
    """
    decimal_places = 0
    is_negative = False
    for i in range(0, len(line) - 1):
        if isinstance(line[i], np.int64):
            if line[i] < 0:
                is_negative = True
            continue
        elem = line[i]
        temp = len(np.format_float_positional(elem).split('.')[1])

        if np.format_float_positional(elem).split('.')[1] == '':
            if temp < 1:
                temp = 1
        if temp > decimal_places:
            decimal_places = temp
        if elem < 0.0:
            is_negative = True
    return 10 ** decimal_places, is_negative
