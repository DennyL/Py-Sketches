def non_uniques(data: list) -> list:
    """
    From chekio.
    The function returns an iterable of non-unique
    elements of a list given
    """
    
    non_uniques = []
    for item in data:
        if data.count(item) > 1:
            non_uniques.append(item)
    
    return non_uniques
