"""
This is exaple.py module.

It supplies reverse() function. E.g.:

>>> reverse('awesome!')
'!emosewa'
"""


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

