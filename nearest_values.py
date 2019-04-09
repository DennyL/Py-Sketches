################
# from checkio #
################

"""
Find the nearest value to the given one.
You are given a list of values as set form and a value for which you need to find the nearest one.
For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17,
and we need to find the nearest value to the number 9.
If we sort this set in the ascending order, then to the left of number 9 will be number 7
and to the right - will be number 10.
But 10 is closer than 7, which means that the correct answer is 10.

A few clarifications:
If 2 numbers are at the same distance, you need to choose the smallest one;
The set of numbers is always non-empty, i.e. the size is >=1;
The given value can be in this set, which means that it’s the answer;
The set can contain both positive and negative numbers, but they are always integers;
The set isn’t sorted and consists of unique numbers.
"""

def nearest_value(values: set, one: int) -> int:
    
    # we may turn the set into a list, append the given number to it
    # and to sort it. Then, we may find out the nearest numbers
    # by calculating indexes of neighbour numbers
    # and comparing their values
    data = list(values)
    data.append(one)
    data = sorted(data)
    
    nearest1 = data[data.index(one)-1] if data.index(one) > 0 else data[data.index(one)+1]
    nearest2 = data[data.index(one)+1] if data.index(one) < len(data)-1 else nearest1
    
    distance1 = abs(nearest1 - one)
    distance2 = abs(nearest2 - one)
    
    if distance1 == distance2: return min(nearest1, nearest2)
    
    return nearest1 if distance1 < distance2 else nearest2


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
