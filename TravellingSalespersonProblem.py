from TSPsetup import TSPGrid
import plotMap as pm 
from NearestNeighbor import NearestNeighbor
from GeneticAlgorithm import GeneticAlgorithm
import distanceHelpers as dh


problem_space = TSPGrid(10,9)
setOfPoints = problem_space.citiesToVisit

# Genetic Algorithm
maxEpochs = 1000 
populationSize = 5000
mutationPercent = 0.01
ga = GeneticAlgorithm(setOfPoints, maxEpochs, populationSize, mutationPercent)
pm.PlotRoute(setOfPoints, ga.path, "Genetic Algorithm", dh.getDistanceOfRoute(ga.path, setOfPoints) )

# Nearest Neighbor Algorithm
nn = NearestNeighbor(setOfPoints) 
pm.PlotRoute(setOfPoints, nn.path, "Nearest Neighbor", dh.getDistanceOfRoute(nn.path, setOfPoints) )

