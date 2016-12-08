class ArithmeticCircuit:
    def __init__(self, name):
        self.name = name
        self.x = None
        self.y = None
        self.cOut = None
        self.s = None
    def __repr__(self):
        return "{0} with name {1}".format(self.__class__, self.name)

    def getOutput(self):
        self.getInput()
        return self.performArithmetic()


class HalfAdder(ArithmeticCircuit):
    def __init__(self, name):
        ArithmeticCircuit.__init__(self, name)

    def performArithmetic(self):
        self.s = 1 if self.x + self.y == 1 else 0
        self.cOut = 1 if self.x + self.y == 2 else 0
        return "Sum: %s\nCarry: %s" %(self.s, self.cOut)

    def getInput(self):
        self.x = int(input("Enter value for pin X: "))
        self.y = int(input("Enter value for pin Y: "))

class FullAdder(ArithmeticCircuit):
    def __init__(self, name):
        ArithmeticCircuit.__init__(self, name)
        self.cIn = None


    def getInput(self):
        self.x = int(input("Enter value for pin X: "))
        self.y = int(input("Enter value for pin Y: "))
        self.cIn = int(input("Enter value for pin Cin: "))

    def performArithmetic(self):
        self.s = 1 if self.x or self.y or self.cIn or (self.x and self.y and self.cIn) else 0
        self.cOut = 1 if (self.x and self.y) or (self.x and self.cIn) or (self.y and self.cIn) else 0

        return "Sum: %s\nCarry: %s" %(self.s, self.cOut)


g1 = HalfAdder('g1')
print(g1)
print(g1.getOutput())

g2 = FullAdder('g1')
print(g2)
print(g2.getOutput())