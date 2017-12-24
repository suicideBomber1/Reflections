import collections


def find_it(seq):
    count = collections.Counter(seq)
    for i in count.keys():
        if count[i] % 2 == 1:
            return i


result = find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
print(result)
