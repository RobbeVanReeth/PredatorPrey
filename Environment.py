import Hunter
import Prey


class Environment:
    def __init__(self):
        self.predators = []
        self.prey = []

    def addPredator(self, predator):
        self.predators.append(predator)
    def spawnPredator(self):
        self.predators.append(Hunter.Hunter())
    def addPrey(self, prey):
        self.prey.append(prey)

    def getPredator(self):
        return self.predators

    def getPrey(self):
        return self.prey

