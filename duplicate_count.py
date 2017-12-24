import collections


def duplicate_count(text):
    n = collections.Counter(text.lower())
    count = 0
    for i in n.values():
        if i > 1:
            count += 1
    return count


result = duplicate_count("Indivisibilities")
print(result)
