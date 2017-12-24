def race(v1, v2, d):
    time = []
    v = v2 - v1
    if v1 >= v2:
        return None
    else:
        h = d // v
        time.append(h)
        x = d % v
        m = (x * 60) // v
        time.append(m)
        y = (x * 60) % v
        s = (y * 60) // v
        time.append(s)

    return time


result = race(720, 850, 70)
print(result)
