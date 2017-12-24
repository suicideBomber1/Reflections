def namelist(names):
    l = [i['name'] for i in names]
    if len(l) <= 1:
        return ''.join(l)
    else:
        last_two = ' & '.join(l[-2:])
        first = [i + ',' for i in l[:-2]]
        first.append(last_two)
        first = ''.join(first)
        return first


names = {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}
result = namelist(names)
print(result)
