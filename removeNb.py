def removNb(n):
    l = []
    sum = 0.5 * n * (n + 1)
    for i in range(1, n + 1):
        if (sum - i) % (i + 1) == 0 and int((sum - i) // (i + 1)) <= n:
            l.append((i, int((sum - i) // (i + 1))))

    return l


result = removeNb(26)
print(result)
