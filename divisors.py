def divisors(n):
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            opposite = n // i
            if opposite != i:
                d.append(opposite)
    d = sorted(d)
    if d == []:
        return str(n) + " is a prime number"
    else:
        return d


result = divisors(13)
print(result)
