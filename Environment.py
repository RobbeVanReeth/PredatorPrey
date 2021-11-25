from Prey import Prey as prey
from Hunter import Hunter as pred


class Environment:
    def __init__(self):
        self.predators = []
        self.preys = []

    def breed(self):
        self.addPrey(prey=prey(age=1, birthrate=1, maxAge=6, width=200, height=200, env=self))

    def getPredatorAtLocation(self, x, y):
        for pr in self.predators:
            if pr.positionX == x and pr.positionY == y:
                return pr
        return None

    def printLocationsPrey(self):
        for pr in self.preys:
            print(f"{pr.positionX}, {pr.positionY}")

    def addPredator(self, predator):
        self.predators.append(predator)

    def removePrey(self, prey):
        self.preys.remove(prey)

    def addPrey(self, prey):
        self.preys.append(prey)

    def getPreyAtLocation(self, x, y):
        """
        Finds and removes prey at location x,y
        :param x:
        :param y:
        :return:
        """
        for pr in self.preys:
            if pr.positionX == x and pr.positionY == y:
                print("Position found")
                self.preys.remove(pr)
                return True
        print("Prey not found, not gonna remove.")
        return False

    def isCloseToPrey(self, posX, posY):
        for pr in self.preys:
            if pr.positionX != posX and pr.positionY != posY:
                if abs(pr.positionX - posX) <= 3:
                    if abs(pr.positionY - posY) <= 3:
                        print(f"Found prey at location:{pr.positionX},{pr.positionY}, I'm at {posX},{posY}")
                        return pr.positionX, pr.positionY
        return None, None

    def isCloseToPredator(self, posX, posY):
        for pr in self.predators:
            if pr.positionX != posX and pr.positionY != posY:
                if abs(pr.positionX - posX) <= 4:
                    if abs(pr.positionY - posY) <= 4:
                        print(f"Found mating partner at:{pr.positionX},{pr.positionY}, I'm at {posX},{posY}")
                        return pr.positionX, pr.positionY
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
        self.addPredator(predator=pred(energyLevel=100, age=1, maxAge=50, reproduceEnergy=10,
                                           energyPerPrayEaten=20, width=200, height=200, env=self))
