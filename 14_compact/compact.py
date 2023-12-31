def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    answer = []
    for val in lst:
        if bool(val) == True:
            answer.append(val)

    return answer

#solution uses computation for this