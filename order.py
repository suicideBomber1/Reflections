def order(sentence):
    l = sentence.split()
    s = {}
    for i in l:
        for j in i:
            if j.isdigit():
                s[j] = i

    l = [s[i] for i in sorted(s.keys())]
    return ' '.join(l)


result = order("is2 Thi1s T4est 3a")
print(result)
