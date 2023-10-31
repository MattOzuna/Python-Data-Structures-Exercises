def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    list_phrase = list(phrase)
    list_phrase.reverse()
    answer = ''
    for letter in list_phrase:
        answer = answer + letter
    return answer

    #incorrect
        # return phrase[::-1]
        # can reverse with just by splicing