def reverse(s):
    """Reverse a string.

    >>> reverse('')
    ''
    >>> reverse('Hexlet')
    'telxeH'
    >>> reverse('Barbara Streisand')
    'dnasiertS arabraB'
    """
    return s[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

