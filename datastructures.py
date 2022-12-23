n = 1000
a = list(range(n))
b = dict.fromkeys(range(n))

for i in range(100):
    assert i in a
    assert i in b

def o_one(items):
    return 1

def o_n(items):
    total = 0

    for item in items:
        total += item
    return total


def o_n_squared(items):
    total = 0
    for a in items:
        for b in items:
            total += a * b
        return total


n = 10
items = range(n)
result = o_one(items)

result2 = o_n(items)

result3 = o_n_squared(items)

print(result3)