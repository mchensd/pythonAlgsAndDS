def moveTower(fromPole, toPole, withPole, height):
    if height >= 1:
        moveTower(fromPole, withPole, toPole, height-1)
        moveBase(fromPole, toPole)
        moveTower(withPole, toPole, fromPole, height-1)

def moveBase(fromPole, toPole):
    print("Move disk from %s to %s" %(fromPole, toPole))

moveTower("A", 'C', 'B', 5)
