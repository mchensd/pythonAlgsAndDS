class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performLogic()
        return self.output
        

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate %s:" %(self.getLabel())))
        else:
            return self.pinA.fgate.getOutput()
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate %s:" %(self.getLabel())))
        else:
            return self.pinB.fgate.getOutput()


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
            return int(input("Enter Pin input for gate %s:" %(self.getLabel())))

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performLogic(self):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        return self.pinA and self.pinB

    def setNextPin(self, connector):
        if self.pinA == None:
            self.pinA = connector
        elif self.pinB == None:
            self.pinB = connector
        else:  # both are already set
            raise RuntimeError("Both pins are already set. Check for extraneous connectors.")

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performLogic(self):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        return self.pinA or self.pinB
    
    def setNextPin(self, connector):
        if self.pinA == None:
            self.pinA = connector
        elif self.pinB == None:
            self.pinB = connector
        else:  # both are already set
            raise RuntimeError("Both pins are already set. Check for extraneous connectors.")
class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performLogic(self):
        self.pin = self.getPin()
        return 0 if self.pin else 1

class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate
        tgate.setNextPin(self)

g1 = AndGate("g1-and")
g2 = AndGate("g2-and-gate")
g3 = OrGate("g3-or")
c = Connector(g1, g3)
c2 = Connector(g2, g3)
print(g3.getOutput())

