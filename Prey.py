import random


class Prey:
    """
    Properties: Age, 2D position, Birth-rate, Max-age
    Behavior:
        - Moves randomly in the environment
        - Checks if it needs to reproduce, if so -> create new prey
        - Checks if it reached its maximum age, if so -> kill
    """

    def __init__(self, age, posX, posY, birthrate, maxAge,
                 width, height):
        self.age = age
        self.positionX = posX
        self.positionY = posY
        self.birthrate = birthrate
        self.maxAge = maxAge
        self.width = width
        self.height = height

    def moveRandomly(self):
        direction = random.randint(0, 3)
        if direction == 0:  # Move one step to the right unless at max width then go left
            if self.getPosX() != self.getWidth():
                self.positionX += 1
                print("Prey moved right")
            else:
                self.positionX -= 1
                print("Prey moved left")

        elif direction == 1:  # Move one step to the left unless at start then go right
            if self.getPosX() != 0:
                self.positionX -= 1
                print("Prey moved left")
            else:
                self.positionX += 1
                print("Prey moved right")

        elif direction == 2:  # Move one step to the top unless at top then move down
            if self.getPosY() != self.getHeight():
                print("Prey moved up")
                self.positionY += 1
            else:
                self.positionY -= 1
                print("Prey moved down")

        elif direction == 3:  # Move one step to the bottom unless at bottom then move up
            if self.getPosY() != 0:
                self.positionY -= 1
                print("Prey moved down")
            else:
                self.positionY += 1
                print("Prey moved up")

    def getPosX(self):
        return self.positionX

    def getPosY(self):
        return self.positionY

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def checkAge(self):
        if self.age == self.maxAge:
            print("Max age reached -> bye bye")
            return True

    def step(self):
        """
        Moves randomly
        Check if reproduce
        Verify maximum age if so -> kill

        :return: (kill, breed)
        """

        self.age += 1
        self.moveRandomly()
        breed = self.checkBreed()
        if self.checkAge():
            return False, breed

        return True, breed

    def checkBreed(self):
        """
        If random number is lower than birthrate -> breed
        :return: Breed Boolean
        """
        randomNumber = round(random.random()*100)
        if randomNumber < self.birthrate:
            return True
        return False
