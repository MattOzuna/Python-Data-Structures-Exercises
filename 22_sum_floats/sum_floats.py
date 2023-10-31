def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>>     
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    answer = 0

    for num in nums:
        if isinstance(num, float):
            answer += num
    
    return answer