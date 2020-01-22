from TSPsetup import TSPGrid
from NearestNeighbor import NearestNeighbor
from GeneticAlgorithm import GeneticAlgorithm

problem_space = TSPGrid(20,20)
problem_space.printPrettyGrid()
setOfPoints = problem_space.citiesToVisit

print("Genetic Algorithm")
ga = GeneticAlgorithm(setOfPoints, 1000, 1000, 0.01)
print(f"{ga.path} = {ga.getDistanceOfRoute(ga.path, setOfPoints)}")
print("Nearest Neighbor")
nn = NearestNeighbor(setOfPoints) 
print(f"{nn.path} = {ga.getDistanceOfRoute(nn.path, setOfPoints)}")