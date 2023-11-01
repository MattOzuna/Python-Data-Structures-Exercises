def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    words = phrase.split(' ')
    answer = ''

    for word in words:
        answer = answer + word.capitalize() + ' '
    
    return answer.strip()

#there is a buitl in function for this .title()