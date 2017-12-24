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


def valid_parentheses(symbol):
    # your code here
    s = Stack()
    i = 0
    string = ''
    for j in symbol:
        if ord(j) == 40 or ord(j) == 41:
            string += j
        else:
            continue
    print(string)

    while i < len(string):
        if string[i] == '(':
            s.push(string[i])

        else:
            if s.is_empty() != True:
                s.pop()
            else:
                return False
        i += 1
    if s.is_empty():
        return True
    else:
        return False
