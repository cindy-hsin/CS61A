"""
Q9: Interleaved Sum
Write a function interleaved_sum that similarly computes the sum of a sequence of terms from 1 to n, 
but uses different functions to compute the terms for odd and even numbers. 
Do so without using any loops or testing in any way if a number is odd or even. 
(You may test if a number is equal to 0, 1, or n.)
"""

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """

    #the iterative version:
    """
    total = 0
    x = 1
    while x <= n:
        if x % 2 == 0:
            total += even_term(x)
        else:
            total += odd_term(x)
        x += 1
    return total
    """

    #the recursion version 1: leap of faith
    """
    def sum(x, formula):
        if x == n:
            return formula(n)
        elif x == n - 1:
            return formula(n - 1)
        else:
            return sum(x + 2, formula) + formula(x)

    return sum(1, odd_term) + sum(2, even_term)
    """

    #the recursion version 2 (solution from github): 
    #use helper function to track "count" & "total", and return the readily calculated "total" in base case.
    #NOTE: "1- index" can be used to track parity(odd-even) of the current term
    def helper(total, count, is_even, odd_term, even_term): #is_even: the index of term
        if count > n:
            return total
        elif is_even == 0:
            total += odd_term(count)
        else:
            total += even_term(count)
        return helper(total, count + 1, 1 - is_even, odd_term, even_term) #1- is_even: track parity

    return helper(0, 1, 0, odd_term, even_term)
