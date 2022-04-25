"""
Evelyn Goodman
CSE 163 AC
This program implements the functions for HW2 using pandas
"""


def species_count(data):
    """
    returns the number of unique pokemon species
    in the dataset as determined by the name attribute
    """
    num_unique = data["name"].nunique()
    return num_unique


def max_level(data):
    """
    returns a 2-element tuple of the (name, level) of the pokemon
    with the highest level in the dataset
    """
    max_level = data["level"].max()
    max_index = data["level"].idxmax()
    max_name = data.loc[max_index]['name']
    return (max_name, max_level)


def filter_range(data, lower, upper):
    """
    The function returns a list of the names of pokemon whose level fall
    within the bounds in the same order that they appear in the dataset
    """
    mask = (data['level'] >= lower) & (data['level'] < upper)
    x = data[mask]
    return list(x['name'])


def mean_attack_for_type(data, poke_type):
    """
    returns the average attack for all the pokemon in
    the dataset with the given type
    """
    mask = data['type'] == poke_type
    type_mask = data[mask]
    if type_mask.empty:
        return None
    else:
        return type_mask['atk'].mean()


def count_types(data):
    """
    returns a dictionary representing for each pokemon type
    the number of pokemon of that type
    """
    return dict(data.groupby('type')['type'].count())


def mean_attack_per_type(data):
    """
    returns a dictionary representing for each pokemon
    and the average attack of that type.
    """
    return dict(data.groupby('type')['atk'].mean())