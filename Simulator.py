from Hunter import Hunter as pred
from Prey import Prey as prey
import Environment
import matplotlib.pyplot as plt

steps_for_Graph = []
preys_for_Graph = []
predators_for_graph = []
env = Environment.Environment()
file = open("logging.txt", "w")
file.close()
for i in range(100):
    env.addPrey(prey=prey(age=1, birthrate=23, maxAge=6, width=200, height=200, env=env))
for i in range(20):
    env.addPredator(pred(energyLevel=100, age=1, maxAge=20, reproduceEnergy=30,
                         energyPerPrayEaten=20, width=200, height=200, env=env))

isFinished = False

for i in range(0, 100):

    if isFinished:
        print("FINISHHHHHH")
        break
    for predator in env.getPredators():
        if predator.step():
            a, b = env.isCloseToPredator(predator.positionX, predator.positionY)
            if a is not None and b is not None:
                if predator.energyLevel > predator.reproduceEnergy:
                    print("WOOHOOW, gonna MATE")
                    predator.energyLevel -= predator.reproduceEnergy
                    env.breedPredators()

            x, y = env.isCloseToPrey(predator.positionX, predator.positionY)
            print(x,y)
            if x is not None and y is not None:
                print("AWWYEAH, gonna eat!!")
                predator.eat()
                env.getPreyAtLocation(x, y)
            predator.printInfo()
        else:
            env.predators.remove(predator)
            print("Removed a predator.")
            if len(env.getPredators()) == 0:
                print("No more predators, simulation over.")

                isFinished = True
    for prey in env.getPreys():
        if prey.step():
            prey.printInfo()
        else:
            env.preys.remove(prey)
            print("Removed a prey.")
    if (len(env.getPredators()) + len(env.getPreys()) >= 20000) or (len(env.getPreys()) == 0) or \
            (len(env.getPredators()) == 0):
        isFinished = True
        print("Finishing this simulation, since one of the populus is empty or too large.")
    with open('logging.txt', 'a') as f:
        f.write("\nStep: " + str(i) + "\nPredators: " + str(len(env.getPredators())) + "\n"
                + "Prey: " + str(len(env.getPreys())))
        f.close()
    steps_for_Graph.append(i)
    preys_for_Graph.append(len(env.getPreys()))
    predators_for_graph.append(len(env.getPredators()))

plt.plot(steps_for_Graph, preys_for_Graph, label="prey")
plt.plot(steps_for_Graph, predators_for_graph,  label="predator")
plt.title=("Predator vs Prey population")
plt.legend()
plt.show()
print("No more predators, simulation over")
