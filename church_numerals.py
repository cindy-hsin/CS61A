"""
Q7: Church numerals
The logician Alonzo Church invented a system of representing non-negative integers entirely using functions. 
The purpose was to show that functions are sufficient to describe all of number theory: 
if we have functions, we do not need to assume that numbers exist, but instead we can invent them.

Your goal in this problem is to rediscover this representation known as Church numerals. 
Here are the definitions of zero, as well as a function that returns one more than its argument:
"""
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))
"""
First, define functions one and two such that they have the same behavior as successor(zero) and successsor(successor(zero)) respectively, 
but do not call successor in your implementation.

Next, implement a function church_to_int that converts a church numeral argument to a regular Python integer.

Finally, implement functions add_church, mul_church, and pow_church that perform 
addition, multiplication, and exponentiation on church numerals.

"""

def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    # 自己的錯解
    """
    if n == zero:
        return 0
    else:
        integer = 1
        test = successor(zero)
        while n(f)(x) != test(f)(x): #運行時Error: name 'f' is not defined
            integer += 1
            test = successor(test)
        return integer
    """
    # 正解
    # input →               →wanted output
    # zero → zero(f)(x) = x, → 0
    # one → one(f)(x) = f(x), → 1
    # two → two(f)(x) = f(f(x)) → 2
    # So if x = 0, and f is a function that returns one more than x → Done!

    def increment(x):
        return x + 1
    return n(increment)(0)


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(n(f))(x)
    #最优解： 不需要引入argument x
    #return lambda f: m(n(f))

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: n(m)(f)(x)
    #最优解： 不需要引入argument f和x
    #return n(m)
