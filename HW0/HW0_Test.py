"""
Evelyn Goodman
CSE 163 AC
This program tests the functions for HW0
"""
import hw0


from cse163_utils import assert_equals


def test_total():
    """
    Evaluation statements that check the expected answer
    against the actual output of hw0.total
    returns errors given in cse163_util function "assert_equals".
    """
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    # if n in negative, return None
    assert_equals(None, hw0.total(-6))


def test_funky_sum():
    """
    Evaluation statements that check the expected answer
    against the actual output of hw0.funky_sum
    returns errors given in cse163_util function "assert_equals".
    """
    # two tests from spec
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(2.2, hw0.funky_sum(1, 3, 0.6))
    # seems likely we might mess up 0 or negative num
    # or greater than 1
    assert_equals(5, hw0.funky_sum(5, 8, 0))
    assert_equals(1, hw0.funky_sum(1, 2, -6))
    assert_equals(2, hw0.funky_sum(1, 2, 6))


def test_swip_swap():
    """
    Evaluation statements that check the expected answer
    against the actual output of hw0.swip_swap
    returns errors given in cse163_util function "assert_equals".
    """
    # test cases from spec
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    # making sure the function word for longer words
    assert_equals('msiisiispps', hw0.swip_swap('mississippi', 'i', 's'))
    # passing an empty string as source will result in an empty string
    assert_equals('', hw0.swip_swap('', 'a', 'b'))


def main():
    """
    runs all three testing functions to ensure functions
    are working properly.
    """
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()