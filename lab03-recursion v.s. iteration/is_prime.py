"""
Q8: Is Prime
Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise.
Assume n > 1. We implemented this in Discussion 1 iteratively, now time to do it recursively!

Hint: You will need a helper function! 
Remember helper functions are useful if you need to keep track of more variables than the given parameters, 
or if you need to change the value of the input.
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
