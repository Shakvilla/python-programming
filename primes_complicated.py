import itertools


def primes_complicated():
    sieved = dict()
    i = 2

    while True:
        if i not in sieved:
            yield i
            sieved[i * i] = [i]
        else:
            for j in sieved[i]:
                sieved.setdefault(i + j, []).append(j)
            del sieved[i]

        i += 1
result = list(itertools.islice(primes_complicated(), 10))
print(result)