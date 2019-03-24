###############################
#        from checkio         #
# Solution by Denys Lozinskyi #
###############################

def visualization(func):
    '''
        simple decorator for visualization of turning one data into another
    '''
    def wrapper(data):
        a = func(data)
        print(data, ' -> ', a)
        return a
    return wrapper
        

@visualization     
def arabs2romans(number):
    '''
        converts arab numbers into the latins
    '''
    
    if not 0 < number < 4000: raise Exception('your number must be in range between 0-4000')
     
    tab = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
    ]
    
    result = ''
    for arab, roman in tab:
        while number >= arab:
            result += roman
            number -= arab
    return result



assert arabs2romans(6) == 'VI'
assert arabs2romans(76) == 'LXXVI'
assert arabs2romans(499) == 'CDXCIX'
assert arabs2romans(3888) == 'MMMDCCCLXXXVIII'
assert arabs2romans(2019) == 'MMXIX'
assert arabs2romans(50) == 'L'
assert arabs2romans(61) == 'LXI'
assert arabs2romans(3) == 'III'
