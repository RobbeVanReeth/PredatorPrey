from Prey import Prey as prey
from Hunter import Hunter as pred


class Environment:
    def __init__(self):
        self.predators = []
        self.preys = []
        self.locationsPrey = []
        self.locationsPredator = []

    def breed(self):
        self.addPrey(prey=prey(age=1, birthrate=17, maxAge=20, width=200, height=200, env=self))

    def getPredatorAtLocation(self,x,y):
        for i in range(len(self.predators)):
            if self.predators[i].positionX == x and self.predators[i].positionY == y:
                return self.predators[i]
        return None

    def getPreyAtLocation(self, x, y):
        """
        Returns prey from certain location x, y
        :param x: X location of prey
        :param y: Y location of prey
        :return: prey if present
        """
        i = 0
        for p in self.preys:
            i += 1
            if p.positionX == x and p.positionY == y:
                return p, i
        return None

    def printLocationsPrey(self):
        for i in range(len(self.locationsPrey)):
            print(self.locationsPrey[i])

    def addPredator(self, predator):
        self.predators.append(predator)
        self.locationsPredator.append((predator.positionX, predator.positionY))

    def removePrey(self, prey):
        self.locationsPrey.remove(prey)
        self.preys.remove(prey)

    def addPrey(self, prey):
        self.preys.append(prey)
        self.locationsPrey.append((prey.positionX, prey.positionY))

    def isCloseToPrey(self, posX, posY):
        for x, y in self.locationsPrey:
            if x != posX and y != posY:
                if abs(x - posX) <= 1:
                    if abs(y - posY) <= 1:
                        print(f"Found prey at location:{x},{y}, I'm at {posX},{posY}")

                        return True
        return False

    def isCloseToPredator(self, posX, posY):
        for x, y in self.locationsPredator:
            if x != posX and y != posY:
                if abs(x - posX) <= 1:
                    if abs(y - posY) <= 1:
                        print(f"Found mating partner at:{x},{y}, I'm at {posX},{posY}")
                        return x, y
        return None, None

    def getPredator(self, i):
        return self.predators[i]

    def getPrey(self, i):
        return self.preys[i]

    def getPredators(self):
        return self.predators

    def getPreys(self):
        return self.preys

    def hasPredators(self):
        if len(self.predators) >= 1:
            return True
        else:
            return False

    def breedPredators(self):
        self.addPredator(predator=pred(energyLevel=10, age=1, maxAge=50, reproduceEnergy=10,
                                           energyPerPrayEaten=20, width=200, height=200, env=self))
