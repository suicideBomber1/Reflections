def mode(num_list):
    return max(num_list, key=num_list.count)


def find_missing(s):
    diff = []
    n = len(s)
    for i in range(n - 1):
        diff.append(s[i + 1] - s[i])
    d = mode(diff)
    first = s[0]
    last = s[n - 1]
    ar_ser = [i for i in range(first, last, d)]
    m = set(ar_ser) - set(s)
    for i in m:
        return i


result = find_missing([1, -2, -5, -8, -11, -14, -20, -23, -26])
print(result)
