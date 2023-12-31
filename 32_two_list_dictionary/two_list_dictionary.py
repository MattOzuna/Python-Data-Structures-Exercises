def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    answer = {}

    for key in keys:
        answer.setdefault(key)
        index = keys.index(key)

        if len(keys) <= len(values):
            answer[keys[index]] = values[index]
        
        if len(keys) > len(values):
            for index in range(len(values)):
                answer[keys[index]] = values[index]
        
#the solution is awesome

    
    
    
    
    
    
    
    
    # if len(keys) == len(values):
    #     for index in range(len(keys)):
    #         answer[keys[index]] = values[index]
    
    # if len(keys) < len(values):
    #     for key in keys:
    #         answer.setdefault(key)
        
    #     for index in range(len(values)):
    #         answer[keys[index]] = values[index]

        
       
       
        # for val in range(len(keys)-len(values)):
        #     values.append(None)

        # for index in range(len(keys)):
        #     answer[keys[index]] = values[index]



    return answer