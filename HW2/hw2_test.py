"""
Evelyn Goodman
CSE 163 AC
This program tests the functions for HW2
"""


import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

SPEC_TEST_FILE = "/home/pokemon_test.csv"
MY_TEST_FILE = "/home/evelyn_test.csv"


def test_species_count(spec_test_df, spec_test_data, my_test_df, my_test_data):
    """
    tests the species_count function
    """
    assert_equals(3, hw2_manual.species_count(spec_test_data))
    assert_equals(3, hw2_pandas.species_count(spec_test_df))
    assert_equals(9, hw2_manual.species_count(my_test_data))
    assert_equals(9, hw2_pandas.species_count(my_test_df))


def test_max_level(spec_test_df, spec_test_data, my_test_df, my_test_data):
    """
    tests the max_level function
    """
    assert_equals(('Lapras', 72), hw2_manual.max_level(spec_test_data))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(spec_test_df))
    assert_equals(('Persian', 87), hw2_manual.max_level(my_test_data))
    assert_equals(('Persian', 87), hw2_pandas.max_level(my_test_df))


def test_filter_range(spec_test_df, spec_test_data, my_test_df, my_test_data):
    """
    tests the filter_range function
    """
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(spec_test_data, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(spec_test_df, 35, 72))
    assert_equals(['Rattata', 'Clefairy', 'Metapod'],
                  hw2_manual.filter_range(my_test_data, 13, 30))
    assert_equals(['Rattata', 'Clefairy', 'Metapod'],
                  hw2_pandas.filter_range(my_test_df, 13, 30))


def test_mean_attack_for_type(spec_test_df, spec_test_data,
                              my_test_df, my_test_data):
    """
    tests the mean_attack_for_type function
    """
    assert_equals(47.5,
                  hw2_manual.mean_attack_for_type(spec_test_data, 'fire'))
    assert_equals(47.5,
                  hw2_pandas.mean_attack_for_type(spec_test_df, 'fire'))
    assert_equals(None,
                  hw2_manual.mean_attack_for_type(my_test_data, 'air'))
    assert_equals(None,
                  hw2_pandas.mean_attack_for_type(my_test_df, 'air'))


def test_count_types(spec_test_df, spec_test_data, my_test_df, my_test_data):
    """
    tests the count_types function
    """
    assert_equals({'fire': 2, 'water': 2},
                  hw2_manual.count_types(spec_test_data))
    assert_equals({'fire': 2, 'water': 2},
                  hw2_pandas.count_types(spec_test_df))
    assert_equals({'normal': 3, 'grass': 2, 'poison': 1, 'bug': 3,
                  'fairy': 1, 'fire': 1, 'rock': 1},
                  hw2_manual.count_types(my_test_data))
    assert_equals({'normal': 3, 'grass': 2, 'poison': 1, 'bug': 3,
                  'fairy': 1, 'fire': 1, 'rock': 1},
                  hw2_pandas.count_types(my_test_df))


def test_mean_attack_per_type(spec_test_df, spec_test_data,
                              my_test_df, my_test_data):
    """
    tests the mean_attack_per_type function
    """
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(spec_test_data))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(spec_test_df))
    assert_equals({'normal': 65.0, 'grass': 168.0, 'poison': 56.0,
                  'bug': 20.0, 'fairy': 33.0, 'fire': 35.0, 'rock': 65.0},
                  hw2_manual.mean_attack_per_type(my_test_data))
    assert_equals({'normal': 65.0, 'grass': 168.0, 'poison': 56.0,
                  'bug': 20.0, 'fairy': 33.0, 'fire': 35.0, 'rock': 65.0},
                  hw2_pandas.mean_attack_per_type(my_test_df))


def main():
    spec_test_df = pd.read_csv(SPEC_TEST_FILE)
    spec_test_data = parse(SPEC_TEST_FILE)
    my_test_df = pd.read_csv(MY_TEST_FILE)
    my_test_data = parse(MY_TEST_FILE)

    test_species_count(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_max_level(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_filter_range(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_mean_attack_for_type(spec_test_df, spec_test_data,
                              my_test_df, my_test_data)
    test_count_types(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_mean_attack_per_type(spec_test_df, spec_test_data,
                              my_test_df, my_test_data)


if __name__ == '__main__':
    main()