def search4vowels(phrase:str) -> set:
    '''Return any vowels found in a supplied phrase.'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) -> set:
    '''Return the supplied letters found in a supplied phrase.'''
    return set(letters).intersection(set(phrase))
