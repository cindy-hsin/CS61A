from lab04 import *

# Q13
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"

    #Iterative solution  ???
    """
    new_lst = []
    for x in lst:
        if type(x) != list:
            new_lst += [x]
        else:
            new_lst
    """
    """
    #Recursive solution(with record)
    new_lst = []
    for x in lst:
        #base case:
        if type(x) != list:
            new_lst += [x]
        #recursive case:
        else:
            new_lst += flatten(x)
    return new_lst
    """

    #Recursive solution(with/ record)
    #base case:
    if lst == []:
        return []
    #recursive case:
    elif type(lst[0]) != list:
        return [lst[0]] + flatten(lst[1:])
    else:
        return flatten(lst[0]) + flatten(lst[1:])

# Q14
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"

    #Iterative solution
    new_lst = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            new_lst += [lst1[0]]
            lst1 = lst1[1:]
        else:
            new_lst += [lst2[0]]
            lst2 = lst2[1:]
    if not lst1:
        return new_lst + lst2
    elif not lst2:
        return new_lst + lst1

    """
    #Recursive solution(with record)
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        new_lst = []
        if lst1[0] < lst2[0]:
            new_lst += [lst1[0]]
            lst1 = lst1[1:]
        else:
            new_lst += [lst2[0]]
            lst2 = lst2[1:]
        return new_lst + merge(lst1, lst2)
    """

    """
    #Recursive solution(with/ record)
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        if lst1[0] < lst2[0]:
            return [lst1[0]] + merge(lst1[1:], lst2)
        else:
            return [lst2[0]] + merge(lst1, lst2[1:])
    """
