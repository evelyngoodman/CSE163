"""
Evelyn Goodman
CSE 163 AC
This program implements the functions for HW0
"""


def funky_sum(a, b, mix):
    """
    This function returns the sum of the two given numbers a, b
    and a parameter number, mix, to determine ratio.
    If mix <= 0, return a, return b if mix >= 1
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n):
    """
    This function returns the sum of the integers
    from 0 (incl) to the parameter n (incl).
    If n is negative, return None
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source, c1, c2):
    """
    This function returns a string with parameters c1 and
    c2 swapped with eachother in a given word (source).
    """
    swapped = ""
    for letter in source:
        if letter == c1:
            swapped += c2
        elif letter == c2:
            swapped += c1
        else:
            swapped += letter
    return swapped