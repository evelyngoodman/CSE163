"""
Evelyn Goodman
CSE 163 AC
This program implements the functions for HW2 without using pandas
"""


def species_count(data):
    """
    returns the number of unique pokemon species
    in the dataset as determined by the name attribute
    """
    unique_set = set()
    for item in data:
        if item['name'] not in unique_set:
            unique_set.add(item['name'])
    return len(unique_set)


def max_level(data):
    """
    returns a 2-element tuple of the (name, level) of the pokemon
    with the highest level in the dataset
    """
    max_level = 0
    max_name = ''
    for row in data:
        if row['level'] > max_level:
            max_level = row['level']
            max_name = row['name']
    return (max_name, max_level)


def filter_range(data, lower, upper):
    """
    The function returns a list of the names of pokemon whose level fall
    within the bounds in the same order that they appear in the dataset
    """
    poke_list = []
    for row in data:
        if row['level'] >= lower and row['level'] < upper:
            poke_list.append(row['name'])
    return poke_list


def mean_attack_for_type(data, poke_type):
    """
    returns the average atk for all the pokemon in
    the dataset with the given type
    If there are no pokemon of the given type, return None
    """
    sum_atk = 0
    count = 0
    for row in data:
        if row['type'] == poke_type:
            sum_atk += row['atk']
            count += 1
    if count == 0:
        return None
    else:
        return sum_atk / count


def count_types(data):
    """
    returns a dictionary representing for each pokemon type
    the number of pokemon of that type
    """
    counts = dict()
    for row in data:
        type = row['type']
        if type in counts:
            counts[type] += 1
        else:
            counts[type] = 1
    return counts


def mean_attack_per_type(data):
    """
    returns a dictionary representing for each pokemon
    and the average attack of that type.
    """
    counts = dict()
    sums = dict()
    for row in data:
        poke_type = row['type']
        if poke_type in counts:
            counts[poke_type] += 1
            sums[poke_type] += row['atk']
        else:
            counts[poke_type] = 1
            sums[poke_type] = row['atk']
        averages = dict()
    for poke_type in counts:
        averages[poke_type] = sums[poke_type] / counts[poke_type]
    return averages