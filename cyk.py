def nonzero_splits(word):
    for i in range(len(word) - 1):
        a = word[:i+1]
        b = word[i+1:]
        yield a, b


def cartesian_product(a, b):
    for x in a:
        for y in b:
            yield (x, y)


def cyk_rec(word, terminals, pairs, cache):
    if len(word) == 1:
        char = word[0]
        if char in terminals:
            ret = [(t, (t, char)) for t in terminals[char]]
            return ret
        else:
            return []

    if word in cache:
        return cache[word]

    productions = []
    for left, right in nonzero_splits(word):
        cart = cartesian_product(
            cyk_rec(left, terminals, pairs, cache),
            cyk_rec(right, terminals, pairs, cache),
        )

        for (left, left_hist), (right, right_hist) in cart:
            lr = (left, right)
            if lr in pairs:
                for prod in pairs[lr]:
                    productions.append((prod, (prod, left_hist, right_hist)))

    cache[word] = productions

    return productions


def cyk(word, terminals, pairs):
    return cyk_rec(word, terminals, pairs, {})


if True:
    terminals = {
        'a': ['A'],
        'b': ['B'],
    }

    pairs = {
        ('A', 'B'): ['S'],
        ('B', 'A'): ['S'],
        ('A', 'S'): ['A'],
        ('B', 'S'): ['B'],
        ('B', 'C'): ['A'],
        ('A', 'D'): ['B'],
        ('A', 'A'): ['C'],
        ('B', 'B'): ['D'],
    }

    word = "baabba"
else:
    terminals = {
        'a': ['A', 'C'],
        'b': ['B'],
    }

    pairs = {
        ('A', 'B'): ['S', 'C'],
        ('B', 'A'): ['A'],
        ('B', 'C'): ['S'],
        ('C', 'C'): ['B'],
    }

    word = "baaba"

cache = {}
res = cyk_rec(word, terminals, pairs, cache)

for tree in res:
    print(tree)
