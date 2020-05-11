#!/usr/bin/env python
'''
assert_example.py

An example for why using assert to test for expected condition is bad.

You can "turn off" asserts by typing "python -O filename.py" and thus
    bypassing the check.

Expectations when running the code:
python assert_example.py -> assert is read and prints out it error
python -O assert_example.py -> assert is not read and prints a standard error


'''

def divide_me(number_1=None, number_2=None):
    assert number_1 != None, "Error: you did not provide a numerator"
    assert number_2, "Error: you did not provide a denominator"
    assert number_2 != 0, "Error: you can't divide by 0"

    return number_1/number_2


divide_me(number_1=1.0)
