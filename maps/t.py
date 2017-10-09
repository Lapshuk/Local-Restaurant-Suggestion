def map_and_filter(s, map_fn, filter_fn):
    """Returns a new list containing the results of calling map_fn on each
    element of sequence s for which filter_fn returns a true value.

    >>> square = lambda x: x * x
    >>> is_odd = lambda x: x % 2 == 1
    >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)
    [1, 9, 25]
    """
    # BEGIN Question 0
    return [map_fn(elem) for elem in s if filter_fn(elem)]
    # END Question 0

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.

    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    # BEGIN Question 0
    return min([key for key in d], key = lambda x: d[x])
    # END Question 0

def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.

    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    # BEGIN Question 0
    return [list(elem) for elem in zip(range(start,len(s)+start), s)]
    # END Question 0
