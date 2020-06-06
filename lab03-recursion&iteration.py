def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    
    #the iterative version
    """
    print(n)
    total = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
        total += 1
    return total
    """
    
    #the recursive version 1: Leap of Faith
    #base case: When n=1, print(n) and return: total += 1
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1
    

    #the recursive version 2: use Helper Function to keep track of total(number of terms).
    """
    def helper(total, n):
        print(n)
        if n == 1:
            return total
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        return helper(total + 1, n)
    return helper(1, n)
    """


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    #the i
    """
    x = n - 1
    while x > 1:
        if n % x == 0:
            return False
        else:
            x = x - 1
    return True
    """

    def check(x):
        if x <= 1:
            return True
        elif n % x == 0:
            return False
        else:
            return check(x - 1)
    return check(n - 1)
