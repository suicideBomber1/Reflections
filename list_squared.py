def list_squared(m, n):
    l = []
    for i in range(m, n + 1):
        s = sum_sq_fac(i)
        sqrt_sum = s**0.5
        if sqrt_sum == int(sqrt_sum):
            l.append([i, s])

    return l


def factors(N):
    div_list = []
    for n in range(1, int((N + 1) ** 0.5) + 1):
        if N % n == 0:
            div_list.append(n)
            opposite = N // n
            div_list.append(opposite)

    return set(div_list)


def sum_sq_fac(n):
    d = factors(n)
    sum = 0
    for i in d:
        sum += (i**2)
    return sum


result = list_squared(1, 250)
print(result)
