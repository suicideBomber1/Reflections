# Time Complexity O(n**2)
###################################################
'''
def removNb(n):
    l = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (i + j + (i * j) == (0.5 * n * (n + 1))):
                l.append((i, j))

    return l

'''
###################################################


def removNb(n):
    l = []
    sum = 0.5 * n * (n + 1)
    for i in range(1, n + 1):
        if (sum - i) % (i + 1) == 0:
            while int((sum - i) // (i + 1)) <= n:
                l.append((i, int((sum - i) // (i + 1))))

    return l


result = removNb(26)
print(result)
