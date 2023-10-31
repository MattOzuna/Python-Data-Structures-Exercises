def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    answer = ''

    for char in phrase.lower():
        if phrase.index(char) == 0:
            answer = answer + char.upper()

        if phrase[phrase.index(char)-1] == ' ':
            answer = answer + char.upper()
            
        else:
            answer = answer + char
    
    return answer
