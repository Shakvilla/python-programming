def filter_modulo(items, modulo):
    for item in items:
        if item % modulo:
            yield item
result = list(filter_modulo(range(20), 2))
print(result)