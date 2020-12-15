#!/usr/bin/env python

'''
assert_example.py

An example for why using assert to test for expected condition is bad.

You can "turn off" asserts by typing "python -O filename.py" and thus
    bypassing the check.

Expectations when running the code in a bash terminal:
python assert_example.py -> assert is read and prints out it error
python -O assert_example.py -> assert is not read and program runs
'''


def simple_print(number_1=None, number_2=None):
    assert number_1 != None, "Error: you did not provide a numerator"
    assert number_2 != None, "Error: you did not provide a denominator"
    assert number_2 != 0, "Number 2 can't be zero"

    print(number_1, number_2)


simple_print(number_2=0.0)
