def sol_equa(n):
    d = []
    r = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            opposite = n // i
            d.append([i, opposite])
    for i in range(len(d)):
        x = (d[i][0] + d[i][1]) * 0.5
        y = (d[i][1] - d[i][0]) * 0.25
        if (int(x) == x) & (int(y) == y):
            r.append([int(x), int(y)])

    return r


result = sol_equa(90005)
print(result)
