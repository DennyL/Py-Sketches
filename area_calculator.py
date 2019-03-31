####################
# Solution by D.L. #
####################


def abridger(data, direction=1):
    """
    removes empty lines, i.e.
    those not containing "#"
    until it finds one containing at least one "#"
    """
    for i in data[::direction]:
        if "#" not in i:
            data.remove(i)
        else:
            break            
    return data


def area(sketch):
    """
    calculates the area for building a house
    at the sketch given
    """
    field = sketch.split()

    # removing empty horizontal lines
    # but ONLY from the top:
    field = abridger(field)
    # and from the bottom:
    field = abridger(field, -1)

    # rotating the area and removing empty vertical lines
    # doing that the same way - ONLY from the top and the bottom
    rotated = list(zip(*field))
    rotated = abridger(rotated)
    rotated = abridger(rotated, -1)

    # now, we have a "fair" area for building a house
    # stored in a list of tuples of equal length,
    # where the length of a list is the area's width,
    # and the length of a tuple is the area's height or vice versa.
    # Thus, the area of the field for building represented here
    # may be found as multiplication of these two lengths.
    return 0 if len(rotated) == 0 else len(rotated[0]) * len(rotated)



################
# testing area #
################

assert area(
    '''00000
0###0
#0000
#00#0
####0
00000''') == 16

assert area('''00000 0#000''') == 1

assert area(
    '''00000
0#0#0
000#0''') == 6

assert area(
    '''0000000
##00##0
######0
##00##0
#0000#0''') == 24

assert area(
    '''0000000000
#000##000#
##########
##000000##
0000000000''') == 30

assert area(
    '''0000
0000
#000''') == 1

assert area(
    '''0000
0000''') == 0

assert area(
    '''0##0
0000
#00#''') == 12

