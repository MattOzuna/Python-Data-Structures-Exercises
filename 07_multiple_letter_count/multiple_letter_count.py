def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    answer = {}
    for char in phrase:
        count = 0
        for letter in phrase:
            if letter == char:
                count += 1
        answer[char] = count
    return answer

    #incorrect
    # counter = {}

    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1

    # return counter