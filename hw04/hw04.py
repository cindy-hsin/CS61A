HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    #intersection(st,ave) is constructor (of intersection type data)
    #street(inter) and avenue(inter) are selector
    #不需理解constructor和selector是如何implemented的
    #直接用这个abstraction→constructor, selector 及之间的关系 即可
    return abs(street(a)-street(b)) + abs(avenue(a)-avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    #自己解 #和答案解相比，引入了s中各项的”每一个约数”，计算量大。
    """
    def divisors(n):
        return [1] + [x for x in range(2,n) if n % x == 0]
    def perfect_square(n): #return True if it is a perfect square
        for x in divisors(n):
            if n // x == x:
                return True
        return False
    return [int(x**0.5) for x in s if perfect_square(x)]
    """
    #答案解
    return [round(x**0.5) for x in s if round(x**0.5)**2 == x]
    #NOTE: filter expression中的Round若不加，结果错误。（30会被判定为perfect square） （30.0 == 30 evaluates to True）


def g(n):
    """
    G(n) = n,                                       if n <= 3
    G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
    """
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        list = [1,2,3]
        """
        i = 4
        while i <= n:
            item = list[2] + 2 * list[1] + 3 * list[0]
            list = [list[1],list[2],item]
            i += 1
        """

        for _ in range(4,n+1):
            item = list[2] + 2 * list[1] + 3 * list[0]
            list = [list[1],list[2],item]
        return item

        #list = [1,2,3]
        #i = 4 → item = 10
        #      → list = [2,3,10]
        #i = 5 → item = 10 + 2*3 + 3*2 = 22
        #      → list = [3,10,22]

    #答案解：概念类似list,只不过用了Multiple assignment
    """
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c
    """


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    #先计算n之前的所有bracket index,并判断离n最近的bracket index是第奇数个or第偶数个bracket index
    def br_index(n):
        return [x for x in range(1,n) if x % 7 ==0 or has_seven(x)]

    def upward(n):
        if len(br_index(n)) % 2 == 0: #length is even number
            return 1  #处在上升段，故第n项 = 第n-1项 + 1
        else:
            return -1 #处在下降段，故第n项 = 第n-1项 - 1

    if n <= 7: #base case
        return n
    else: #recursive case
        return pingpong(n - 1) + upward(n)

    #答案解1：连 list comprehension都没用→真正的no assignment statement?
    """
    def pingpong2(n):
    if n <= 7:
        return n
    return direction(n) + pingpong(n-1)

    #判断所在段调性也用recursion
    def direction(n): #direction(n):n的调性，即n处于上升段 还是 n处于下降段，也即从n-1到n是 +1 还是 -1
        if n < 7:
            return 1
        if (n-1) % 7 == 0 or has_seven(n-1):
            return -1 * direction(n-1)  #继1-is_even可记录1,0的交替变化后，*(-1)可记录正负的交替变化。
        return direction(n-1)  #若第n-1项的index不是bracket index，则n和n-1处于同一（调性）段
    """

    #答案解2：从sequence的头开始，k记录index，p记录各项value,up记录调性。
    #把这些需要track的量作为函数argument，传下去，直至index==n时return当前的p.(没有用leap of faith版本的recursion)
    #形式：Mutual Recursion
    """
    #pingpong_next用于计算下一项
    def pingpong_next(k, p, up):
        if k == n:
            return p
        if up:
            return pingpong_switch(k+1, p+1, up)
        else:
            return pingpong_switch(k+1, p-1, up)

    #pingpong_switch用于判断是否该转换调性
    def pingpong_switch(k, p, up):
        if k % 7 == 0 or has_seven(k):
            return pingpong_next(k, p, not up)
        else:
            return pingpong_next(k, p, up)

    return pingpong_next(1, 1, True)
    """

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def trace1(fn):
    def traced(x, y):
        print('Calling', fn, 'on arguments', x, y)
        return fn(x, y)
    return traced
#Tree recursion → 本质同Counting  Partitions。
#分类讨论：1). use at least one 2**max_power;
#        2). do not use 2**max_power
# number of ways = numer of 1) + number of 2)
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"

    #计算小于等于n的最大2-power:
    max_power = 0
    while 2**max_power <= amount:
        max_power += 1
    max_power = max_power -1

    @trace1
    def count(amount, max_power): #recursion
        #base case
        if amount < 0:
            return 0
        elif amount == 0:
            return 1
        elif max_power == 0:
            return 1
        #recursive case
        else:
            return count(amount - 2**max_power, max_power) + count(amount, max_power - 1)
    return count(amount, max_power)


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
