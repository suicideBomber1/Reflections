# def runoff(voters):
#     l = {}
#     key = []
#     for i in range(len(voters)):
#         key.append(voters[i][0])
#         keys = set(key)

#     l = dict.fromkeys(keys, 0)

#     for i in range(len(voters)):
#         l[voters[i][0]] += 1
#     print(l)
#     while True:
#         max_votes = max(l.values(), default=0)
#         min_votes = min(l.values(), default=0)
#         if l == {}:
#             return None
#             break
#         elif max_votes >= (sum(l.values()) * 0.5):
#             for k in l:
#                 if l[k] == max_votes:
#                     return k
#                     break
#         else:
#             for k in list(l):
#                 if l[k] == min_votes:
#                     del l[k]


# result = runoff([["a", "c", "d", "e", "b"],
#                  ["e", "b", "d", "c", "a"],
#                  ["d", "e", "c", "a", "b"],
#                  ["c", "e", "d", "b", "a"],
#                  ["b", "e", "a", "c", "d"]])
# print(result)

def runoff(voters):
	l = {}
	keys= []
	for i in range(len(voters)):
		key.append(voters[i][0])
		keys = set(key)

	l = dict.fromkeys(keys, 0)

    for i in range(len(voters)):
        l[voters[i][0]] += 1

    




























