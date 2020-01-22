import random 
import distanceHelpers as dh

class GeneticAlgorithm():
  """ supply a set of points and this genetic algorithm will find the fastest route between them """
  def __init__(self, setOfPoints: list, maxEpochs: int, populationSize: int, mutationPercent: float ):

    population = self.initialPopulation(populationSize, len(setOfPoints))
    epoch = 0 
    while epoch < maxEpochs: 
      matingPool = self.createMatingPool(population,setOfPoints)
      # print(matingPool)
      if self.converged(population) or len(matingPool) == 0:
        break
      else:
        population = self.evolve(matingPool, mutationPercent, populationSize)
        # print(population)
        epoch += 1
      if epoch % 100 == 0:
        print(f"Epoch={epoch}")
    # is it worth searching for the fastest route in population?
    self.path = population[0]

  def initialPopulation(self, popSize: int, numCities: int) -> list:
    """ create an initial population of size popSize and with numCities in length each """
    population = []
    while len(population) < popSize: 
      randomRoute = list(range(1,numCities))
      population.append([0] + random.sample(randomRoute, len(randomRoute)) )
    return population


  def getDistanceOfRoute(self, route: list, cities: list) -> float:
    """ return the distance traveling the specified route """
    distance = 0
    for i in range(len(route)-1):
      distance += dh.pythagoreanDistance(cities[route[i]], cities[route[i+1]])
    return distance

  def createMatingPool(self, population: list, cities: list) -> list:
    """ based on fitness, create a matingPool of most viable candidates for next epoch """
    matingPool = []
    distances = []
    for i in population:
      distances.append(self.getDistanceOfRoute(i,cities))
    avgDistance = sum(distances) / len(population)
    for j in range(len(population)):
      if distances[j] < avgDistance:
        howFit = (round(avgDistance) - round(distances[j]) + 1) * 3 
        for _ in range(howFit):
          matingPool.append(population[j])
    return matingPool

  def mate(self, parent1: list, parent2: list) -> list:
    """ Combine two routes to create a child route."""
    child = [] 
    misfitGene = []
    for i in range(0,len(parent1)):
      if parent1[i] == parent2[i]:
        child.append(parent1[i])
      else:
        misfitGene.append(parent1[i])
        misfitGene.append(parent2[i])
        child.append(None)
    
    for j in range(len(child)):
      if child[j] == None:
        stop = False 
        while stop == False:
          a = misfitGene.pop(0)
          if a not in child:
            child[j] = a 
            stop = True
    return child 
  
  # def mutate(self, child: list) -> list:
  #   """ reorder child to add diversity into gene pool """
  #   mutant = child  
  #   i = mutant.pop(random.randrange(1,len(child)))
  #   mutant.append(i)
  #   return mutant

  def evolve(self, matingPool: list, mutationPercent: float, populationSize: int) -> list:
    """ create a new generation by pulling from matingPool and mating """
    # TODO: add in mutation 
    evolution = []
    for _ in range(populationSize):
      parent1 = matingPool[random.randrange(len(matingPool))]
      parent2 = matingPool[random.randrange(len(matingPool))]
      child = self.mate(parent1, parent2)
      # oddsOfMutation = random.randrange(100)
      # if oddsOfMutation <= mutationPercent*100:
      #   child = self.mutate(child)
      evolution.append(child)
    return evolution 

  def converged(self, population: list) -> bool:
    """ check to see if the population is all the same """
    ctr = 0
    for i in population:
      if i == population[0]:
        ctr+=1
    if ctr == len(population):
      return True 
    else: 
      return False

  