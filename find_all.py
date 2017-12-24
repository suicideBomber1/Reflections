
l = []
n = ''


def find_all(sum_dig, digs):
    if sum_dig == 0 & digs == 0:
        return n
    n = ''

    for i in range(1, 10):
        sum = sum_dig - i
        n += str(i)
        find_all(sum, digs - 1)


# i, j, k (3 integers who sum is fixed)


result = find_all(10, 3)
print(result)
