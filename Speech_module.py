################
# from checkio #
################

"""
Stephen's speech module is broken.
This module is responsible for his number pronunciation.
He has to click to input all of the numerical digits in a figure,
so when there are big numbers it can take him a long time.
Help the robot to speak properly and increase his number
processing speed by writing a new speech module for him.
All the words in the string must be separated by exactly
one space character. Be careful with spaces - it's hard to see
if you place two spaces instead one.

Input: A number as an integer.
Output: The string representation of the number as a string.
"""

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = []
    if number >= 100:
        hundreds = number//100
        result.append(FIRST_TEN[hundreds-1])
        result.append("hundred")
        number -= (100*hundreds)
    if number >= 20:
        o_tens = number//10
        result.append(OTHER_TENS[o_tens-2])
        number -= (10*o_tens)
    if number >= 10:
        s_tens = number%10
        result.append(SECOND_TEN[s_tens])
    if 0 < number < 10:
        result.append(FIRST_TEN[number-1])
        
    return " ".join(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
