class LogicGate:  # general logic gate
    def __init__(self, n):
        self.label = n
        self.output = None

    def __str__(self):
        return("Gate with name %s" %(self.label))
    def getLabel(self):
        return self.label

    def getOutput(self):  # user calls this function
        self.output = self.performLogic()  # performs the specific logic
                                            # of particular gate
        return self.output
        

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None
        self.connectorA = None
        self.connectorB = None

    def getPinA(self):  # called as part of getOutput -> performLogic
        if self.connectorA == None:  # check if any connectors
            return int(input("Enter Pin A input for gate %s:" %(self.getLabel())))
        else:  # if there are connectors, get  the output from the fgate
            return self.connectorA.fgate.getOutput()
    def getPinB(self):
        if self.connectorB == None:
            return int(input("Enter Pin B input for gate %s:" %(self.getLabel())))
        else:
            return self.connectorB.fgate.getOutput()


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None
        self.connector = None

    def getPin(self):
        if self.connector == None:
            return int(input("Enter Pin input for gate %s:" %(self.getLabel())))
        else:
            return self.connector.fgate.getOutput()

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performLogic(self):
    
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        self.output = self.pinA and self.pinB
        return self.output  # returns to getOutput  

    def setConnector(self, connector):
        if self.connectorA == None:
            self.connectorA = connector
        elif self.connectorB == None:
            self.connectorB = connector
        else:  # both are already set
            raise RuntimeError("Both pins are already set. Check for extraneous connectors.")

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performLogic(self):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()
        self.output = self.pinA or self.pinB
        return self.output
    
    def setConnector(self, connector):
        if self.connectorA == None:
            self.connectorA = connector
        elif self.connectorB == None:
            self.connectorB = connector
        else:  # both are already set
            raise RuntimeError("Both pins are already set. Check for extraneous connectors.")
class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performLogic(self):
        self.pin = self.getPin()  # inherited from unarygate
        return 0 if self.pin else 1

    def setConnector(self, connector):
        if self.connector == None:
            self.connector = connector

class NandGate(AndGate):
    def __init__(self, n):
        AndGate.__init__(self, n)
    def performLogic(self):
        return 0 if super().performLogic() else 1
    
        

class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate
        print(self.fgate)
        self.tgate.setConnector(self)

g1 = AndGate("g1-and")
g2 = AndGate("g2-and-gate")
g3 = OrGate("g3-or")
g4 = NotGate('g4')
c = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
g4.getOutput()
