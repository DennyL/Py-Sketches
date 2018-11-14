def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # First of, let's create a dict out of chars of a line given.
    # Since keys in a dict are always unique, we'll obtain it containing
    # letters with their single occurence in a line given
    # that is why we sign value "1" to each of them:
    
    char_tab = dict.fromkeys(line, 1)

    # let's also install a counter of repeated occurences

    counter = 1

    # Now let's look for repeated occurences
    # comparing every second character of the line with its neighbour char
    # on its left (so that we couldn't run out of indexes).
    # When we find out that same chars stay together
    # we increase a corresponding key by 1.
    # Also, we increase value a counter.
    # A counter will help us control values of corresponding keys
    # so that if we'll have a line like this "sdaanmaaann" with 2 substrings
    # containing "a", value of "a" key in a dict had
    # not a total amount of "a"s in a whole string,
    # but length of the longest substring that contains "a"s
    
    for i in range(1, len(line)):
        if line[i-1] == line[i]:
            counter += 1
            if char_tab.get(line[i]) < counter:
                char_tab.update({line[i]:char_tab.get(line[i]) + 1})
        else:
            counter = 1
    
    # If argument was an empty string, a dict will also be empty.
    # Let's handle this case:
    
    if len(char_tab) == 0:
        return 0
    
    max_key = max(char_tab, key=char_tab.get)
    
    return char_tab[max_key]
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sffdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
