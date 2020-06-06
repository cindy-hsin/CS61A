def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    
    #the iterative version
    """
    x = n - 1
    while x > 1:
        if n % x == 0:
            return False
        else:
            x = x - 1
    return True
    """
    
    #the recursive version: 
    #use helper function check(x), since the input needs to be changed (start checking from n-1, instead of n)
    def check(x):
        if x <= 1:
            return True
        elif n % x == 0:
            return False
        else:
            return check(x - 1)
    return check(n - 1)
