from Hunter import Hunter
from Prey import Prey as prey
import Environment
test = Hunter(energyLevel=10, age=1, posX=5, posY=5,  maxAge=10, reproduceEnergy=10,
              energyPerPrayEaten=10, width=10, height=10)
test2 = Hunter(energyLevel=10, age=1, posX=6, posY=6,  maxAge=10, reproduceEnergy=10,
               energyPerPrayEaten=10, width=10, height=10)
test3 = Hunter(energyLevel=10, age=1, posX=6, posY=6,  maxAge=10, reproduceEnergy=10,
               energyPerPrayEaten=10, width=10, height=10)
test4 = prey(age=1, posX=5, posY=5, birthrate=0.17, maxAge=10,
                 width=10, height=10)


env = Environment.Environment()
env.addPredator(test)
env.addPrey(test4)


for i in range(0, 100):
    for predator in env.getPredator():
        predator.step()
    for prey in env.getPrey():
        prey.step()

