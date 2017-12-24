class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def valid_braces(symbol):

    s = Stack()
    pair = {}
    pair['('] = ')'
    pair['['] = ']'
    pair['{'] = '}'
    i = 0
    while i < len(symbol):
        if symbol[i] == '(' or symbol[i] == '[' or symbol[i] == '{':
            s.push(symbol[i])
        elif symbol[i] == pair[s.peek()]:
            s.pop()
        else:
            # if not s.is_empty():
            #     s.pop()
            # else:
            return False
        i += 1

    if s.is_empty():
        return True
    else:
        return False


print(valid_braces("[(])"))
