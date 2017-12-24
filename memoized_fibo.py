def fibonacci(n):
    result = {}

    if n <= 2:
        ans = 1
        result[n] = ans

    elif n in result:
        ans = result[n]
    else:
        ans = fibonacci(n - 1) + fibonacci(n - 2)
        result[n] = ans

    return ans


print(fibonacci(70))
