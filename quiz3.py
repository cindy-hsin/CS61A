#Discussion3 Quiz 1(a)
def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """
    #Solution1: Works for total ==0, but logically contradictory for 2 base cases
    """
    if total % m == 0 or total % n == 0:
        return True
    elif total < min(n, m):
        return False
    return has_sum(total - m, n, m) or has_sum(total - n, n, m)
    """
    #Solution2: Do one more subtraction, making the "very" base case. → Logically correct for total == 0:
    if total == 0:
        return True
    elif total < 0:
        return False
    return has_sum(total - m, n, m) or has_sum(total - n, n, m)

def trace1(fn):
    def traced(x, y):
        print('Calling', fn, 'on arguments', x, y)
        return fn(x, y)
    return traced

#难点：理解pmin,pmax的意义，及如何decrement pmin,pmax
#pmin, pmax: the minimum and maximum pages we could've printed.
#Discussion3 Quiz 1(b)
def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between 180 and 200 copies total
    True
    """
    @trace1
    def copies(pmin, pmax):
        if lower <= pmin and pmax <= upper:
            return True
        #Wrong solution: won't work for copies(55,120)→ should be "True"(Printer 1 * 2), but in face returns "False"
        #elif (lower <= pmin <= upper and upper < pmax) or (pmin <= lower <= pmax and upper > pmax) or pmin >= upper:
            #return False
        #Correct solution:
        elif pmax > upper:
            return False
        return copies(pmin + 50, pmax + 60) or copies (pmin + 130, pmax + 140)
    return copies(0, 0)




#Tree
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

#Return a list of all leaves of the input tree
def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        return tree(label(t),[increment_leaves(b) for b in branches(t)])

def increment(t):
    #trick: 不需要specify base case(is_leaf)
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
    """
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def tree_max(t):
    return max([label(t)] + [tree_max(b) for b in branches(t)])

def find_path(tree,x):
    if label(tree) == x:
        return [x]
    elif is_leaf(tree) and label(tree) !=x :# x is not in tree
        return None
    else:
        for b in branches(tree):
            if find_path(b,x):
                return [label(tree)] + find_path(b,x)


def prune(t, k):
    if k == 0 or is_leaf(t):
        return tree(label(t))
    else:
        return tree(label(t), [prune(b, k - 1) for b in branches(t)])


def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))
def binarize_branches(bs):
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), binarize_branches(rest)]
    else:
        return [right_binarize(b) for b in bs]

def print_tree(t, indent = 0):
    print('  '* indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

from datetime import date
t = date(2020,9,1)
