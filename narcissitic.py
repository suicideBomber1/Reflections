def narcissistic(value):
    l = [i for i in str(value)]
    count = 0
    for i in l:
        count += int(i)**(len(l))
    if count == value:
        return True
    else:
        return False


result = narcissistic(4887)
print(result)
