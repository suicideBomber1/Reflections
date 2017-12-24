def anagrams(word, words):
    an = []
    for i in words:
        if len(i) == len(word) and sorted(set(list(word))) == sorted(set(list(i))):
            an.append(i)
    return an


result = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(result)
