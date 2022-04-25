"""
Evelyn Goodman
CSE 163 AC
This program implements the functions for HW1
"""


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n, m):
    """
    returns the number of digits in n parameter that
    are divisible by m parameter.
    returns 0 if m is 0.
    """
    counts = 0
    n = abs(n)
    if m == 0:
        return 0
    elif n == 0:
        return 1
    while n > 0:
        digit = n % 10
        if digit % m == 0:
            counts += 1
        n //= 10
    return counts


def is_relatively_prime(n, m):
    """
    returns true is n and m and relatively prime
    to eachother and false if not.
    """
    factor = 0
    while m != 0:
        n, m = m, (n % m)
        factor = n
    return factor == 1


def travel(directions, x, y):
    """
    return a tuple that indicates the new position after
    following the directions starting from the given x, y.
    any characters that are not 'N', 'E', 'W', or 'S'
    (ignoring letter-casing) should be ignored
    """
    string = directions.lower()
    for item in string:
        if item == 'n':
            y += 1
        elif item == 'w':
            x -= 1
        elif item == 'e':
            x += 1
        elif item == 's':
            y -= 1
    coordinates = (x, y)
    return coordinates


def reformat_date(date, current, target):
    """
    returns a new string with the date formatted in the target format
    """
    sep_date = date.split("/")
    sep_curr = current.split("/")
    sep_target = target.split("/")
    reformat = {}
    result = ""
    for i in range(len(sep_curr)):
        reformat[sep_curr[i]] = sep_date[i]
    for item in sep_target:
        for key in reformat:
            if key == item:
                result += reformat[key]
        result += "/"
    return result[:len(result) - 1]


def longest_word(file_name):
    """
    returns the longest word in the file with which line it appears on,
    if the file is empty or there are no words, return None
    """
    longest = ''
    num_line = 0
    longest_line = 0
    with open(file_name) as f:
        lines = f.readlines()
        if not lines:
            return None
        for line in lines:
            num_line += 1
            words = line.split()
            for word in words:
                if len(word) > len(longest):
                    longest = word
                    longest_line = num_line
    return f'{longest_line}: {longest}'


def get_average_in_range(integer_list, low, high):
    """
    returns the average of all values within the list that lie
    in the given range from low (inclusive) to high (exclusive).
    if there are no values within given range, return 0.
    """
    total = 0.0
    count = 0.0
    for num in integer_list:
        if num >= low and num < high:
            count += 1
            total += num
    if total == 0:
        return 0
    return (total / count)


def mode_digit(n):
    """
    returns the digit that appears most frequently in that number,
    if there are two numbers with same frequency, return the digit
    with the greatest value.
    """
    counts = {}
    n = abs(n)
    if n == 0:
        return 0
    else:
        while n > 0:
            digit = n % 10
            if digit in counts:
                counts[digit] += 1
            else:
                counts[digit] = 1
            n //= 10
    max_key = 0
    max_value = 0
    for item in counts:
        if counts.get(item) > max_value:
            max_value = counts.get(item)
            max_key = item
        elif counts.get(item) == max_value:
            max_key = max(item, max_key)
    return max_key