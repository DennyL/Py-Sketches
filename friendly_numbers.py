def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    FROM Checkio. Solution by Dennis Lozinskyi. No Decimal module
    """
    
    # We will need to access powers from a list.
    # Aiming that, we set a counter, value of which is pointing at an index of a power
    # in the list that we need.
    power_tag = 0
    
    # Then, if we are given decimals, we may need to add zeros
    # to the number. It's easier to do, if the number is a float
    if decimals: number = float(number)
    
    # Now, if the number is smaller than the base, we merely return it
    # taking into account a number of decimals, if one is given
    if abs(number) / base < 1: return str(number) + "0"*(decimals-1) + powers[power_tag] + suffix
    
    # Otherwise, we run a loop a loop with the following condition:
    while abs(number) / base >= 1 and power_tag < (len(powers)-1):
        power_tag += 1
        number = round(number) / base        
    number = round(number, decimals) if decimals else int(number)
    
    if type(number) == float and len(str(number).split(".")[1]) < decimals:
        number = str(number) + "0" * (decimals-1)

    return str(number) + powers[power_tag] + suffix

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == "12.000M"
    assert friendly_number(10**32) == "100000000Y"
    assert friendly_number(42, powers=["u","d"], suffix="-n") == '42u-n'
    print("The function has successfully passed all tests")
