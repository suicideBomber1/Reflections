

class Calculator():

    def evaluate(self, string):
        return round(eval(string), 12)


print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
