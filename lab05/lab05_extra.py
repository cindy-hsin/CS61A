from lab05 import *
## Optional Questions ##

# pyTunes (optional)

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> country_tunes = tree('country_tunes',
    ...                  [tree('country',
    ...                    [tree('jason aldean',
    ...                       [tree('johnny cash')]),
    ...                     tree('johnny cash',
    ...                       [tree('hurt')])])])
    >>> new_country = add_song(country_tunes, 'ring of fire', 'johnny cash')
    >>> print_tree(new_country)
    country_tunes
      country
        jason aldean
          johnny cash
        johnny cash
          hurt
          ring of fire
    """
    "*** YOUR CODE HERE ***"
    #思路：从root开始找label为category且is_leaf==False的node,在以此node为root的tree的branch中再加song这个leaf
    #注意：……因最终要求return a new tree,所以不能在branches的list中append一个tree，而是要用到tree constructor去构建一个新tree
    if label(t) == category and not is_leaf(t):
        return tree(label(t), branches(t) + [tree(song)])
    else:
        return tree(label(t), [add_song(b, song, category) for b in branches(t)])

def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    "*** YOUR CODE HERE ***"
    #运用list comprehension的filter功能，在create branch list时就直接略过label为target的branch，不创建那一支branch
    #recursive case和 base case统一
    return tree(label(t), [delete(b, target) for b in branches(t) if label(b)!=target])

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie','ha', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'ha', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['ha']
    >>> table['.']
    ['We']
    """
    #把prev作为每次loop最后的替换变量(且初始值是'.')是聪明的做法
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else: table[prev].append(word)
        prev = word
    return table

    #若是把succ作为每次loop最后的替换变量，则会复杂许多
    """
    table={}
    succ = tokens[1]
    for i in range(len(tokens)):
        if tokens[i] not in table:
            table[tokens[i]] = [succ]
        else: table[tokens[i]].append(succ)
        if 2 + i <= len(tokens) - 1:
            succ = tokens[2 + i]
        else:
            succ = tokens[0]
    # WARNING: 当i = len(tokens)-2, tokens[i] = 倒数第二个, tokens[2 + i] = tokens[len(tokens)]已超出范围
    return table
    """

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)
