def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    count = 0

    for value in lst:
        if search_term == value:
            count += 1
            
    return count

# use count method
# return lst.count(search_term)