def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_count = {}
    num2_count = {}

    for val in str(num1):
            num1_count[val] = str(num1).count(val)

    for val in str(num2):
            num2_count[val] = str(num2).count(val)

    if num1_count == num2_count:
        return True

    return False