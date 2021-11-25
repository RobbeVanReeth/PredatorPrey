import random



class Hunter:
    """
       Properties: Age(0-50), 2D position, Birth-rate, Max-age
       Behavior:
           - Moves randomly in the environment
           - Checks if it needs to reproduce, if so -> create new prey
           - Checks if it reached its maximum age, if so -> kill
       """

    def __init__(self, energyLevel, age, maxAge, reproduceEnergy, energyPerPrayEaten,
                 width, height, env):
        self.energyLevel = energyLevel
        self.reproduceEnergy = reproduceEnergy
        self.age = age
        self.positionX = random.randint(0, width)
        self.positionY = random.randint(0, height)
        self.maxAge = maxAge
        self.energyPerPrayEaten = energyPerPrayEaten
        self.width = width
        self.height = height
        self.env = env

    def eatPray(self):
        self.energyLevel += self.energyPerPrayEaten

    def getPosX(self):
        return self.positionX

    def getPosY(self):
        return self.positionY

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def moveRandomly(self):
        direction = random.randint(0, 3)
        if direction == 0:  # Move one step to the right unless at max width then go left
            if self.getPosX() != self.getWidth():
                self.positionX += 1
                print("Hunter moved right")
            else:
                self.positionX -= 1
                print("Hunter moved left")

        elif direction == 1:  # Move one step to the left unless at start then go right
            if self.getPosX() != 0:
                self.positionX -= 1
                print("Hunter moved left")
            else:
                self.positionX += 1
                print("Hunter moved right")

        elif direction == 2:  # Move one step to the top unless at top then move down
            if self.getPosY() != self.getHeight():
                print("Hunter moved up")
                self.positionY += 1
            else:
                self.positionY -= 1
                print("Hunter moved down")

        elif direction == 3:  # Move one step to the bottom unless at bottom then move up
            if self.getPosY() != 0:
                self.positionY -= 1
                print("Hunter moved down")
            else:
                self.positionY += 1
                print("Hunter moved up")

    def printLocation(self):
        print(f"Location: {self.getPosX()} , {self.getPosY()}")

    def getEnergy(self):
        return self.energyLevel

    def reproduceCheck(self):

        if self.getEnergy() >= self.reproduceEnergy:
            self.reproduce()

    def eat(self):
        self.energyLevel += self.energyPerPrayEaten
        print(f"NOMNOMNOM, energy level is now:{self.energyLevel}")

    def reproduce(self):
        pass

    def checkAge(self):
        if self.age == self.maxAge:
            print("Max age reached -> bye bye")
            return True

    def checkEnergy(self):
        if self.energyLevel == 0:
            print("Zero energy reached -> bye bye")
            return True

    def step(self):
        """
        "Moves randomly"
        "Checks if close to food
        "Check if enough energy to reproduce
        "Check if maximum age reached
        "Check if energy not depleted
        :return: Boolean whether or not target still lives
        """
        self.age += 1
        self.energyLevel -= 1
        self.moveRandomly()
        self.reproduceCheck()
        if self.checkAge():
            return False
        if self.checkEnergy():
            return False
        return True

    def printInfo(self):
        print(f"Age: {self.age} Location: {self.getPosX()},{self.getPosY()}")

