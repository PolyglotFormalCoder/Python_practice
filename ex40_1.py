class DoSomething:
    def __init__(self):
        print("do nothing")

    def printSomething(self):
        print(f"this class prints something: {self.var_x}")

    var_x = 2

some = DoSomething()
some.printSomething()