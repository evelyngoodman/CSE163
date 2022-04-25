"""
Evelyn Goodman
CSE 163 AC
This program tests the functions for HW1
"""
import hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))
    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    """
    tests the count_divisible_digits function.
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    # 2 additional test cases
    assert_equals(5, hw1.count_divisible_digits(246894, 2))
    assert_equals(2, hw1.count_divisible_digits(36, 3))


def test_is_relatively_prime():
    """
    tests the is_relatively_prime function.
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    # 2 additional test cases
    assert_equals(False, hw1.is_relatively_prime(4, 8))
    assert_equals(False, hw1.is_relatively_prime(5, 0))


def test_travel():
    """
    tests the travel function.
    """
    assert_equals((-1, 4), hw1.travel('NW!ewnW', 1, 2))
    # 2 additional test cases
    assert_equals((3, 4), hw1.travel('NESW!n', 3, 3))
    assert_equals((3, 7), hw1.travel('NNEe!s', 1, 6))


def test_reformat_date():
    """
    tests the reformat_date function.
    """
    assert_equals("31/12/1998", hw1.reformat_date("12/31/1998",
                  "M/D/Y", "D/M/Y"))
    # 2 additional test cases
    assert_equals("2008/23/12", hw1.reformat_date("12/23/2008",
                  "M/D/Y", "Y/D/M"))
    assert_equals("2/1978/1", hw1.reformat_date("1/2/1978", "D/M/Y", "M/Y/D"))


def test_longest_word():
    """
    tests the longest_word function.
    """
    assert_equals('3: Merrily,', hw1.longest_word('/home/song.txt'))
    # 2 additional test cases
    assert_equals('3: something', hw1.longest_word('/home/song2.txt'))
    assert_equals('3: something', hw1.longest_word('/home/song2.txt'))


def test_get_average_in_range():
    """
    tests the get_average_in_range function.
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    # 2 additional test cases
    assert_equals(4.0, hw1.get_average_in_range([4, 4, 4], 4, 5))
    assert_equals(16.0, hw1.get_average_in_range([3, 12, 20, 31], 10, 31))


def test_mode_digit():
    """
    tests the mode_digit function.
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    # 2 additional test cases
    assert_equals(2, hw1.mode_digit(111222))
    assert_equals(9, hw1.mode_digit(99123))


def main():
    test_total()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()