def make_readable(seconds):
    h = seconds // 3600
    x = seconds % 3600
    m = x // 60
    s = x % 60
    time = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
    return time


result = make_readable(60)
print(result)
