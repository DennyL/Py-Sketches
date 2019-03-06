def flatlist(array):
    """
       flatlist turns a nested list with any depth of nesting,
       taken as a parameter into a flat list.
       Example: [[2], [4, [5, 6, [6], 6, 6, 6], 7]] -> [2, 4, 5, 6, 6, 6, 6, 6, 7]
       Developed by Dennis Lozinskyi, 03/03/2019
    """
    
    result = [] 
    for i in array:
        if isinstance(i, list):
            result += flatlist(i) 
        else:
            result.append(i)
               
    return result
